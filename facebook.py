from selenium import webdriver
import time


driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.facebook.com/')
driver.maximize_window()

userID = '100070863217471'
passwd = '5xPsmhRYIn'
# user
driver.find_element_by_xpath('//input[@class=\'inputtext _55r1 _6luy\']').send_keys(userID)
# pass
driver.find_element_by_xpath('//input[@data-testid=\'royal_pass\']').send_keys(passwd)
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid=\'royal_login_button\']').click()

print(driver.title)
driver.quit()

