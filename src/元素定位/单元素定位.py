from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_name('wd').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_class_name('s_ipt').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_link_text(u'新闻').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_partial_link_text(u'闻').send_keys('selenium')
driver.quit()

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('#kw').send_keys('selenium')
driver.quit()
