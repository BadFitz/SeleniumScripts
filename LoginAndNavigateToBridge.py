# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re

base_url = "http://inspecttechtest.ahtd.com/"
driver = webdriver.Firefox()

# Login to WebApp
driver.get(base_url)
driver.find_element_by_xpath("//div[2]/div/div/input").send_keys("df27533")
driver.find_element_by_xpath("//div/div[2]/input").send_keys("dave4@4AHTD")
driver.find_element_by_xpath("//div[2]/div/input").click()

a = "test"
print ("|").join(a.split(r"."))


# open "Manage Inventory" page and click "All Assets" "+" button
driver.get(base_url + "/manageassets.aspx")


def click_and_wait(path):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    driver.find_element_by_xpath(path).click()


def wait_and_gather_elements(path):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    return driver.find_elements_by_xpath(path)


# all_assets_path = ("//div[@id='ctl00_ContentPlaceHolder1_tvAssets']" +
#                  "/ul/li/div/span[2]")
assets_top_path = "//td/div/div/ul/li/div/span[2]"
click_and_wait(assets_top_path)

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, all_assets_path))
# )
# driver.find_element_by_xpath(all_assets_path).click()

# handle state bridges
state_bridges_path = "//td/div/div/ul/li/ul/li[2]/div/span[2]"
click_and_wait(state_bridges_path)

districts_path = "//div/ul/li/ul/li[2]/ul/li"
districts = wait_and_gather_elements(districts_path)

for d in districts:
    print d.text

# district2_path = ("//div[@id='ctl00_ContentPlaceHolder1_tvAssets']/ul/li/" +
#                   "ul/li[2]/div/span[2]")
district2_path = "//div/ul/li/ul/li[2]/ul/li[3]/div/span[2]"
click_and_wait(district2_path)
"""
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, district2_path))
)
driver.find_element_by_xpath(district2_path).click()
"""

# district2_county_path = "//div/ul/li/ul/li"
district2_county_path = "//li[2]/ul/li[3]/ul/li"
counties = wait_and_gather_elements(district2_county_path)
"""
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, district2_county_path))
)
counties = driver.find_elements_by_xpath(district2_county_path)
"""

for c in counties:
    print c.text

"""
arkansas_path = "//div[@id='ctl00_ContentPlaceHolder1_tvAssets']/ul/" +
    "li/ul/li[2]/ul/li[2]/div/span[2]"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, arkansas_path))
)
driver.find_element_by_xpath(arkansas_path).click()

driver.find_elements_by_xpath("//div[@id='ct100
"""

# District 2
# /html/body[@class='main_bkgd']/form[@id='aspnetForm']/
# div[@id='divHeaderAndContent']/div[@id='contentWrapper']/table/tbody/
# tr[@id='ContentPlaceHolder1_rowContent']/td/
# table[@id='ContentPlaceHolder1_tblContent']/tbody/tr/
# td[@id='ContentPlaceHolder1_treeTableData']/table/tbody/tr/td/
# div[@id='ContentPlaceHolder1_pnlTree']/
# div[@id='ctl00_ContentPlaceHolder1_tvAssets']/
# ul[@class='rtUL rtLines']/li[@class='rtLI rtFirst rtLast']/
# ul[@class='rtUL']/li[@class='rtLI']

# Arkansas
# /html/body[@class='main_bkgd']/form[@id='aspnetForm']/
# div[@id='divHeaderAndContent']/div[@id='contentWrapper']/table/tbody/
# tr[@id='ContentPlaceHolder1_rowContent']/td/
# table[@id='ContentPlaceHolder1_tblContent']/tbody/tr/
# td[@id='ContentPlaceHolder1_treeTableData']/table/tbody/tr/td/
# div[@id='ContentPlaceHolder1_pnlTree']/
# div[@id='ctl00_ContentPlaceHolder1_tvAssets']/ul[@class='rtUL rtLines']/
# li[@class='rtLI rtFirst rtLast']/ul[@class='rtUL']/li[@class='rtLI']

# driver.find_element_by_xpath(
# "//td/div/div/ul/li/ul/li[2]/div/span[2]").click()
# /html/body[@class='main_bkgd']/form[@id='aspnetForm']/
# div[@id='divHeaderAndContent']/div[@id='contentWrapper']/table/tbody/
# tr[@id='ContentPlaceHolder1_rowContent']/td/
# table[@id='ContentPlaceHolder1_tblContent']/tbody/tr/
# td[@id='ContentPlaceHolder1_treeTableData']/table/tbody/tr/td/
# div[@id='ContentPlaceHolder1_pnlTree']/
# div[@id='ctl00_ContentPlaceHolder1_tvAssets']/ul[@class='rtUL rtLines']/
# li[@class='rtLI rtFirst rtLast']/ul[@class='rtUL']/li[@class='rtLI']
# district2 = driver.find_element_by_xpath(
#    "//td/div/div/ul/li/ul/li[2]"
# ).click()

# district 2
# //td/div/div/ul/li/ul/li[2]/div/span[2]

# Arkansas County
# //li[2]/ul/li[2]/div/span[2]

# Ashley County
# //div/ul/li/ul/li[2]/ul/li[3]/div/span[2]

# district 3
# //td/div/div/ul/li/ul/li[3]/div/span[2]

# districtTree = driver.find_element_by_xpath("//td/div/div/ul/li/ul")
# districts = districtTree.find_elements("li")
# for d in districts:
#     print d
