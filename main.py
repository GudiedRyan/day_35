from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time
import hidden as h

password = os.environ["linkedin_login"]

chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?geoId=102986501&keywords=python%20developer&location=Pennsylvania%2C%20United%20States")

time.sleep(4)
driver.maximize_window()
driver.find_element_by_link_text("Sign in").click()

email = driver.find_element_by_id("username")
email.send_keys("ryan.guide@comcast.net")

password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)


jobs = driver.find_elements_by_css_selector(".job-card-container")

for job in jobs:
    job.click()
    time.sleep(1)

    try:
        save = driver.find_element_by_css_selector(".jobs-save-button button")
        if save.text == "Unsave":
            continue
        else:
            save.click()
    except NoSuchElementException:
        continue


time.sleep(5)
driver.quit()