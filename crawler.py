# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os


class Test1():

  def setup_method(self):
    self.driver = webdriver.Chrome()

  def teardown_method(self):
    self.driver.quit()

  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  

  def test_1(self):
    self.driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252Fuser%252FSigin&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    self.driver.find_element(By.ID, "identifierId").send_keys(os.environ['YOUTUBE_USERNAME'])
    self.driver.find_element(By.ID, "identifierId").send_keys(Keys.ENTER)
    time.sleep(1)
    self.driver.find_element(By.NAME, "password").send_keys(os.environ['YOUTUBE_PASSWORD'])
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    time.sleep(3)
    self.driver.get('https://www.youtube.com/playlist?list=PLpC8pNAHN_NLqT0TExv76jMTdhpQ72hCO') # custom playlist
    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="thumbnail"]').click() # click on the first video
    time.sleep(5)

    title = self.driver.title
    # num_comments = self.driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string').text 
    #num_likes = self.driver.find_element(By.XPATH, '//*[@id="text"]').text 
    #num_dislikes = self.driver.find_element(By.XPATH, '//*[@id="text"]').text
    url = self.driver.current_url

    print('Obtained URL: %s with title: %s' % (url, title))



def inf_wait():
    while True:
        time.sleep(1)


def main():
    crawler = Test1()
    crawler.setup_method()
    crawler.test_1()
    inf_wait()
    #crawler.teardown_method()


if __name__ == '__main__':
    main()
  
