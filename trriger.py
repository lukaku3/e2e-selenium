import unittest, os, csv, re, sys, logging, requests, pprint, json, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from multiprocessing import Pool
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from commons import utils

class Scenario01(unittest.TestCase):
    selenium_server = 'http://192.168.100.101:4444/wd/hub'
    launch_url = 'https://www.google.com'

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor= self.selenium_server,
            desired_capabilities=DesiredCapabilities.CHROME)
        pass


    def test_hello(self):
        driver = self.driver
        driver.get(self.launch_url)
        self.assertIn("Python", driver.title)
        pass


    def tearDown(self):
        self.driver.close()
        pass

if __name__ == "__main__":
    unittest.main()
