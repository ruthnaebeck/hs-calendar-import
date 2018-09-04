import csv
import secrets
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the driver
driver = webdriver.Chrome()

# Go to Events Add Page
driver.get('http://hearthstonecalendar.com/events/add')

# Login
userName = driver.find_element_by_name('name')
passWord = driver.find_element_by_name('pass')
userName.send_keys(secrets.userName)
passWord.send_keys(secrets.passWord)
passWord.submit()

def fillForm(nextEvt):
    # Fill out the form
    eventName.send_keys(nextEvt[0].replace('ï»¿', ''))
    # Marks the event as Open Registration
    openRegistr.click()
    if nextEvt[1] == 'Americas':
        regionAM.click()
    else:
        regionEU.click()
    dateEl.clear()
    dateEl.send_keys(nextEvt[2])
    timeEl.send_keys(nextEvt[3])
    linkTitle.send_keys(nextEvt[4])
    linkUrl.send_keys(nextEvt[5])
    # Click the source button to add HTML to the message body
    sourceBtn.click()
    textBox = driver.find_element_by_css_selector('textarea.cke_source')
    textBox.send_keys(nextEvt[6])
    print(nextEvt[0])

with open('events.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        try:
            WebDriverWait(driver, 15).until(EC.title_contains('Create'))
            print(driver.title)

            # Define form elements
            eventName = driver.find_element_by_id('edit-title')
            openRegistr = driver.find_element_by_id('edit-field-open-registration-und')
            regionAM = driver.find_element_by_id('edit-field-region-und-15')
            regionEU = driver.find_element_by_id('edit-field-region-und-16')
            dateEl = driver.find_element_by_id('edit-field-start-time-und-0-value-datepicker-popup-0')
            timeEl = driver.find_element_by_id('edit-field-start-time-und-0-value-timeEntry-popup-1')
            linkTitle = driver.find_element_by_id('edit-field-links-und-0-title')
            linkUrl = driver.find_element_by_id('edit-field-links-und-0-url')
            saveBtn = driver.find_element_by_id('edit-submit')
            sourceBtn = driver.find_element_by_id('cke_67')
            
            fillForm(row)
            saveBtn.click()
            print('Event added normally!')

        except NoSuchElementException:
            # Sometimes the Source Button isn't found right away
            WebDriverWait(driver, 10)
            sourceBtn = driver.find_element_by_id('cke_67')
            fillForm(next(reader))
            saveBtn.click()
            print('Event added after waiting longer!')
            
        WebDriverWait(driver, 15).until(EC.title_contains(secrets.eventKeyword))
        print(driver.title)
        print('-----------------------')
        driver.get('http://hearthstonecalendar.com/events/add')
