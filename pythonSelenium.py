from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from typing import *

class LoginPage:
    """Class representing a login page."""
    def __init__(self, driver: 'WebDriver'):
        """Create a login page."""
        self.driver = driver
    
    def login(self, username, password) -> 'AccessPage':
        """Login the page on the browser."""
        # Type username and password box.
        usernameBox = self.driver.find_element_by_name("username")
        usernameBox.send_keys(username)
        passwordBox = self.driver.find_element_by_name("password")
        passwordBox.send_keys(password)

        # Click the login button
        loginBtn = self.driver.find_element_by_css_selector("form>button[type=submit]")
        loginBtn.click()

        ### The website actually POST the information to api/auth

        # Return the new page.
        return AccessPage(self.driver)

class AccessPage:
    """Class representing the page after login."""
    def __init__(self, driver: 'WebDriver'):
        """Create the new page"""
        self.driver = driver

    def waitLoad(self, maxSeconds: int):
        """Wait to load the page after login."""
        try:
            # After login, it should have an element of class productSection.
            WebDriverWait(self.driver, maxSeconds).until(partial(Scrapper.hasTargetElement,self.driver, lambda driver: driver.find_element_by_css_selector(".productSection")))
        except:
            # If timeout, it's failed to login.
            raise ValueError("Login failed.")
    
    def getProductList(self) -> str:
        """Get the product list, after login."""
        # Get the JSON file by HTTP request of GET method.
        self.driver.get("https://f2e-test.herokuapp.com/api/products?offset=0&limit=1000")
        try:
            # Wait and load the JSON. In browsers, JSON text should be displayed in a <pre> element.
            WebDriverWait(self.driver, 5000).until(partial(Scrapper.hasTargetElement,self.driver, lambda driver: driver.find_element_by_css_selector("pre")))
        except:
            # If timeout, it's failed to fetch the product list.
            raise ValueError("Product list fetching failed.")
        
        # Return the JSON string.
        return self.driver.find_element_by_css_selector("pre").text

class Scrapper:
    @staticmethod
    def start(username: str, password: str) -> str:
        """Start a scrapper of this challeng."""
        # Create a Chrome webdriver, and go to the login page.
        driver = webdriver.Chrome()
        driver.get("https://f2e-test.herokuapp.com/login")

        ### Use page object model design to continue the test. 
        # Now, a login page should be here.
        loginPage = LoginPage(driver)

        # Login the page and return the new page.
        accessPage = loginPage.login(username, password)

        # Wait the new page to load.
        accessPage.waitLoad(3000)

        # After it's login, get the product list.
        return accessPage.getProductList()

    @staticmethod
    def hasTargetElement(driver: 'WebDriver', functionOfDriver: Callable, _: Any):
        """A static method to check during the loading of a page."""
        try:
            # Try the test with the given web driver, typically check if an element exists.
            functionOfDriver(driver)
            return True
        except:
            return False

if __name__ == "__main__":
    ### Main function to run.
    # Start the scrapper to get the requested JSON file.
    jsonStr = Scrapper.start("f2e-candidate", "P@ssw0rd")

    # Write the json into a file.
    with open("download.json", mode="w", encoding="utf-8") as f:
        f.write(jsonStr)