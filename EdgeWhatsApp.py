from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

class EdgeWhatsApp:   
   
   def __init__(self,driver_path):
      # Set drive
      self.driver = webdriver.Edge(executable_path=driver_path)
      self.driver.get("https://web.whatsapp.com/")
      self.wait = WebDriverWait(self.driver, 600)

   def send_msg(self, to, msg):
      self.quoted_to = '"' + to + '"'
      x_arg = '//span[contains(@title,' + self.quoted_to + ')]'
      group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
      group_title.click()
      message = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
      message.send_keys(msg)
      sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
      sendbutton.click()
      
   def __del__(self):
      self.driver.close() 
