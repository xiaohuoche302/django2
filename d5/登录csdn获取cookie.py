from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://passport.csdn.net/account/login?service=https%3A%2F%2Fwww.csdn.net%2F")

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/h3/a').click()
time.sleep(1)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

driver.find_element_by_xpath('//*[@id="fm1"]/input[8]').click()
time.sleep(2)

cookie = driver.get_cookie()
print(cookie)