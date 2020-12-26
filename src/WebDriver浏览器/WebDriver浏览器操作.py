from selenium import webdriver
import time as t

driver = webdriver.Firefox()
# 窗口最大化
driver.maximize_window()
# 开一个Google页面
driver.get("http://www.google.com")
driver.implicitly_wait(30)
# 查看当前页面地址
print('测试地址为：{0}'.format(driver.current_url))
# 查看当前页面代码
print('当前页面代码为：{0}'.format(driver.page_source))
# 查看当前页面的Title
print('测试页面Title为：{0}'.format(driver.title))
# 休眠
t.sleep(3)
# 页面刷新
driver.refresh()
# 再开一个Bing页面
driver.get('http://www.bing.com')
print('测试地址为：{0}'.format(driver.current_url))
# 休眠
t.sleep(3)
# 回退页面
driver.back()
print('测试地址为：{0}'.format(driver.current_url))
# 回退页面
driver.forward()
print('测试地址为：{0}'.format(driver.current_url))
# 退出
driver.quit()
