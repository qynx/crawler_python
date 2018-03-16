from selenium import webdriver

#driver=webdriver.PhantomJS()
driver=webdriver.PhantomJS()

driver.get('https://www.baidu.com/')

user=driver.find_element_by_id('u')
user.send_keys('username')
passs=driver.find_element_by_id('p')
passs.send_keys('password')

butto=driver.find_element_by_id("login_button")
#butto.click()

print(driver.current_url)