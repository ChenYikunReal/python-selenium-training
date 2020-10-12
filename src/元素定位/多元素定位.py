from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
tag_names = driver.find_elements_by_tag_name('input')
for tag_name in tag_names:
    print(tag_name)
print(type(tag_names))
driver.quit()

# 在搜索框中搜索关键词"selenium"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_elements_by_tag_name('input')[7].send_keys('Selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("file:///D:/PyCharm/selenium-test/src/元素定位/login.html")
classes = driver.find_elements_by_class_name("login")
classes[0].send_keys("Sam")
classes[1].send_keys("123456")
classes[2].click()
driver.quit()
