from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com")
driver.implicitly_wait(30)
driver.save_screenshot('../../data/google1.png')
driver.quit()
