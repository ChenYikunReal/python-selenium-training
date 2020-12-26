from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com")
driver.implicitly_wait(30)
print(driver.get_screenshot_as_png())
driver.quit()
