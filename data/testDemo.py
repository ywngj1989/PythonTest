from selenium import webdriver
web = webdriver.Chrome()
web.get("http://www.baidu.com")
web.find_element_by_xpath('//*[@id="kw"]').send_keys("博客园")
web.find_element_by_xpath('//*[@id="su"]').click()
