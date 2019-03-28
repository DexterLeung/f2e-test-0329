# f2e-test

## Python (Selenium)

[Updated 2019-03-29 12:30]
 
The challenge is written in **Python**. It can be run in command line using `py pythonSelenium.py`, and the target JSON file will be downloaded as `download.json`.

### Requirements

- Chrome
- Python 3.6.5, with package: `selenium` installed.

### Test Environment

- Windows 10
- Python 3.6.5
- Chrome 73
- Command line execution: `py pythonSelenium.py`

### Workflow Details

#### Goal

- Json file with 1000 data attach on EMail <br>
把系統內的 1000筆 資料存儲成 json 格式檔案
- One command scraping the website and store 100 data in json file <br>
寫一個自動化工具，完成 login, 和把系統內的1000筆 資料存儲成 json 格式檔案（附上 github repo 或其他相關檔案）

#### Clues

- Checked with the HTML structure, "Network" tab in F12 tool
- Double-checked with JavaScript inline code

=> "api/auth":  POST request for login information<br>
=> "api/products":  GET request for JSON target data

#### Implementation Overview

- To "scrape browser" as mentioned, I selected selenium because this is a common frontend development/auto-testing tool.
- I selected Python based on prior knowledge.
- Noted using node.js may be another option to create a command line tool on it, but I have no experience in using selenium in node.js; to have a search on this if requested.

*Steps:*
1. Selenium driver to navigate to the login page.
2. Wait until it has been successfully authenticated. (Loading the demo product page.)
3. Selenium driver to navigate to the product API URL with JSON response.
4. Get the text and save as a file.
 
Details can be found in inline references.
 
Thank you,<br/>
Dexter 梁彥聰
