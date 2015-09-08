# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateNewAreas(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://inspecttechtest.ahtd.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_new_areas(self):
        driver = self.driver
        driver.get(self.base_url + "/manageassets.aspx")
        driver.find_element_by_css_selector("a.rmLink.rmFocused > span.rmText").click()
        driver.find_element_by_css_selector("span.rtPlus.rtPlusHover").click()
        driver.find_element_by_css_selector("div.rtMid.rtHover > span.rtIn").click()
        driver.find_element_by_id("ContentPlaceHolder1_Updater").click()
        driver.find_element_by_css_selector("span.rtPlus.rtPlusHover").click()
        driver.find_element_by_css_selector("span.rtPlus.rtPlusHover").click()
        driver.find_element_by_xpath("//div[@id='ctl00_ContentPlaceHolder1_tvAssets']/ul/li/ul/li[2]/ul/li[2]/ul/li[2]/div/span[2]").click()
        driver.find_element_by_id("ContentPlaceHolder1_Updater").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
