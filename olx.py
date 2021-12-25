from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium import webdriver
import time
import string
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from selenium.webdriver import ActionChains


driver = webdriver.Firefox(executable_path="D:\\SGC\\geckodriver.exe")
driver.get(" https://olx.com.pk/mall")

allc=driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div/div/div/button")
mb=driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div/div/div/div/div/ul/li[2]/a/div/span")
m=driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div/div/div/button/svg")
mo=driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/a/b").text
assert(mo,"Mobile", "verified")
actions=ActionChains(driver)



actions.move_to_element(allc).move_to_element(mb).move_to_element(m).click().perform()
