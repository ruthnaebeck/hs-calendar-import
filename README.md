# Hearthstone Calendar Import
Add events to hearthstonecalendar.com with Python & Selenium

- Rename `secrets.py.example` to `secrets.py` and fill in the relevant info

## Windows Install Guide

- Prereq - Have Chrome Installed
- Install Python 3 (comes with pip): https://www.python.org/downloads/
- `pip install selenium`
- Install chocolatey: https://chocolatey.org/install
- `choco install chromedriver`
- Restart cmd and IDLE (if running)
- Try the test python script (replace Firefox with Chrome): https://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example

## Create an events.csv file
The file needs to be comma delimited (or edit main.py) with the following on each line:
- Event Title
- Region (currently setup to work with Americas and Europe)
- Event Date
- Event Time (24 hour format + use your set timezone on the site)
- Link Text (such as "Tournament Registration")
- Link URL
- Body message (currently setup to accept HTML)

## Run it
`python main.py`
