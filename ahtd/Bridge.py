from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bridge:

    def __init__(self, asset_path):
        base_url = "http://inspecttechtest.ahtd.com/"
        self._asset_path = asset_path
        self.driver = webdriver.Firefox()
        self.driver.get(base_url)
        self._login()
        self

    def _login(self):
        userid_input_path = "//div[2]/div/div/input"
        WebDriverWait(self.driver, 10).until(
            EC.prescence_of_element_located((By.XPATH, userid_input_path))
        )
        self.driver.find_element_by_xpath(
            userid_input_path).send_keys("df27533")
        self.driver.find_element_by_xpath(
            "//div[2]/div/div/input").send_keys("df27533")
        self.find_element_by_xpath("//div[2]/div/input").click()

    def _navigate_to_element(self):
        pass
