# webdriver就是我们的模拟浏览器驱动
from selenium import webdriver
# Keys 是用作关键词输入
from selenium.webdriver.common.keys import Keys

# 首先指定driver的浏览器，官方使用的是firefox
driver = webdriver.Chrome()
# 驱动的get方法即为打开这个网页
driver.get("http://www.python.org")
# 确定python在网页源码的title中，即没有打开错网页
assert "Python" in driver.title
# 找到name为"q"的元素
elem = driver.find_element_by_name("q")
# 清除框内内容
elem.clear()
# 在框中填入关键词"pycon"并且发送
elem.send_keys("pycon")
# 获得返回值
elem.send_keys(Keys.RETURN)
# 确定返回值并不是没有找到结果
assert "No results found." not in driver.page_source
# 关闭浏览器驱动，非常重要，不然相当于打开了一个网页没有关闭
driver.close()