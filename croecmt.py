from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://temp-mail.org/vi/")
time.sleep(20)
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div/button[1]').click()
