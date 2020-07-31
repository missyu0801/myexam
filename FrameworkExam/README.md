# QA Exam Framework using pytest
This repository contains example code for the QA exam
using Pytest and can be run in Chrome, Firefox and Edge browsers.
The test can be run in command prompt and generate allure report
 
 `Total of 17 Test Cases`

## Setup
This project requires an up-to-date version of Python 3.
It also uses virtual environment

To set up this project on your local machine:
1. latest Python 3 should be installed in your system
2. Clone it from this GitHub repository.
3. Open command prompt and install `requirements.txt` using pip command `$ pip install -r requirements.txt'
4. Once requirements are installed you can now run the test


## Running Tests
### Run Tests Without Report
Run tests simply using the `py.test` command, by default test will run in Chrome browser

To run in different browser add `--browser_name (selected browser code)` tag after py.test command 
   browser code is "edge" and "firefox"
   
##### Run in Chrome browser
        C:\user directory\FrameworkExam> `py.test`
	
##### Run in Edge browser
	C:\user directory\FrameworkExam> `py.test --browser_name edge`
	
##### Run in Firefox browser
	C:\user directory\FrameworkExam> `py.test --browser_name firefox`

### Run with Allure Report	
To view reports in allure add `--alluredir ./Reports` tag after py.test command
to automatically view report in your browser enter `allure serve ./Reports` 

###### NOTE:
Please clean allure report folder  when running new test instance  
   
##### Run in chrome browser with allure report
	C: user directory\FrameworkExam> `py.test --alluredir ./Reports`
	C: user directory\FrameworkExam> `allure serve ./Reports`
   
##### Run in Edge browser with allure report
	C:\user directory\FrameworkExam> `py.test --browser_name edge --alluredir ./Reports`
	C:\user directory\FrameworkExam> `allure serve ./Reports`
	
##### Run in firefox browser with allure report
	C:\user directory\FrameworkExam> `py.test --browser_name firefox  --alluredir ./Reports`
	C:\user directory\FrameworkExam> `allure serve ./Reports`



## Limitations
The following are not included in the automation test, please expect TC failure if the following scenarios are encountered:
1. Change Language in Login page
2. Handling of robot capcha in browser(please refresh and clear cache)
3. Locked account (wait for 2 hours max to reset test or change password)
4. Forgot password/Change password
