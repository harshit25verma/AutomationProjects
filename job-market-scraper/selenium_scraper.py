from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://justjoin.it")

jobs = driver.find_elements("css selector", "h3")
for job in jobs:
    print(job.text)

driver.quit()
# This script uses Selenium to open the Just Join IT website,
# retrieves all job titles (h3 elements), and prints them to the console.