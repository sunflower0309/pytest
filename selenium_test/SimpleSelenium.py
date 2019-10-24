from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import action_chains
import selenium
# webdriver=webdriver.Chrome()
# webdriver.get('https://bbs.nga.cn/')
# #gbfele=webdriver.find_element_by_link_text("碧蓝幻想")
# gbfele=webdriver.find_elements_by_xpath("//div/div/*[contains(text(),'幻想')]")
# x=webdriver.find_elements(by.By.XPATH,"//div/div/*[contains(text(),'幻想')]")
# print(gbfele==x)

# driver=webdriver.Chrome()
# driver.get('http://css3menu.com/')
# how_menu=driver.find_element_by_xpath("//span/img[contains(@src,'gear')]")
# #how_menu=driver.find_element_by_xpath("//span[contains(text(),'How to')]")
# act=action_chains.ActionChains(driver)
# act.click_and_hold(how_menu).perform()
# act.click(driver.find_element_by_xpath("//div[@class='column']/ul/li/a[contains(text(),'Step')]")).perform()

driver=webdriver.Chrome()
driver.get('https://www.bilibili.com/')
search=driver.find_element_by_xpath("//div[contains(@class,'head-content')]/div/form/input")
search.send_keys("少女歌剧龙骑")
submit=driver.find_element_by_xpath("//div[contains(@class,'head-content')]/div/form/button")
submit.click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
no1=driver.find_element_by_xpath("//div[contains(@id,'all-list')]/div/div[2]/ul/li[1]/a")
#no1=driver.find_element_by_xpath("//ul[contains(@class,'video-list')]/li[1]/a")
no1.click()
driver.switch_to.window(windows[-1])
nolast=driver.find_element_by_xpath("//div[contains(@id,'all-list')]/div/div[2]/ul/li[last()]/a")
nolast.click()
driver.switch_to.window(windows[-1])
switch_page=driver.find_element_by_xpath("//div[contains(@class,'page-wrap')]/div/ul/li[2]/button")
switch_page.click()