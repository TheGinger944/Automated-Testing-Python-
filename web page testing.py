import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestSuite(unittest.TestCase):
  def Before(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://by.wildberries.ru/")

  def Search(self):
    check_searchbox = self.driver.find_element(By.ID, "searchInput")
    self.assertTrue(check_searchbox.is_displayed())
    searchbox = self.driver.find_element(By.ID,"searchInput")
    text = 'беспроводные наушники'
    searchbox.send_keys(text)
    searchbox.send_keys(u'\ue007') # click Enter button
    time.sleep(2)
    new_page = self.driver.find_element(By.XPATH,"//h1[contains(text(),'По запросу «"+text+"» найдено')]")
    self.assertTrue(new_page.is_displayed())

  def PopupTag(self):
    searchbox = self.driver.find_element(By.ID,"searchInput")
    text = 'наушники'
    searchbox.send_keys(text)
    time.sleep(2)
    check_popup_tag = self.driver.find_element(By.XPATH,'//*[@id="searchBlock"]/div[2]')
    self.assertTrue(check_popup_tag.is_displayed())
    tag = self.driver.find_element(By.XPATH, '//*[@id="searchBlock"]/div[2]/div/div/ul[1]/li[1]')
    tag_text = tag.text
    tag.click()
    time.sleep(2)
    new_page = self.driver.find_element(By.XPATH,"//h1[contains(text(),'По запросу «"+tag_text+"» найдено')]")
    self.assertTrue(new_page.is_displayed())
    
  def ClosePopup(self): 
    searchbox = self.driver.find_element(By.ID,"searchInput")
    text = 'наушники'
    searchbox.send_keys(text)
    check_popup_tag = self.driver.find_element(By.XPATH,'//*[@id="searchBlock"]/div[2]')
    self.assertTrue(check_popup_tag.is_displayed())
    popup_close = self.driver.find_element(By.XPATH, '//*[@id="searchBlock"]/div[1]/div[2]/button')
    popup_close.click()
    time.sleep(1)
    self.assertFalse(check_popup_tag.is_displayed())

  def After(self):
    self.driver.quit()
  
test = TestSuite()

test.Before()
test.Search()
#test.PopupTag()
#test.ClosePopup()
test.After()
