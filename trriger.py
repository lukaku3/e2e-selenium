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
        #self.driver = webdriver.Remote(
        #   command_executor= self.selenium_server,
        #    desired_capabilities=DesiredCapabilities.CHROME)
        #self.capabilities = DesiredCapabilities.FIREFOX.copy()
        #self.capabilities['platform'] = "WINDOWS"
        #self.capabilities['version'] = "10"
        pass

    def setUpBrowser(self, type):
        #pprint.pprint(self.capabilities)
        if type is 'ie':
            self.driver = webdriver.Remote(command_executor= self.selenium_server,
                desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())

        elif type is 'edge':
            self.driver = webdriver.Remote(command_executor= self.selenium_server,
                desired_capabilities=DesiredCapabilities.EDGE.copy())
        elif type is 'firefox':
            self.driver = webdriver.Remote(command_executor= self.selenium_server,
                desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        else:
            capabilities=DesiredCapabilities.CHROME.copy()
            capabilities['platform'] = "WINDOWS"
            capabilities['version'] = "10"
            capabilities['maxInstances'] = 10
            self.driver = webdriver.Remote(command_executor= self.selenium_server,
                desired_capabilities=capabilities)
                #desired_capabilities=DesiredCapabilities.CHROME)


    def test_hello(self):
        self.setUpBrowser('chrome')
        driver = self.driver
        driver.get(self.launch_url)
        self.assertIn("Google", driver.title)
        if driver.find_element(By.CSS_SELECTOR, "img#hplogo") is None:
            #----
            pass
        #self.assertEqual(1, 0, "broken")
#        driver.close()

    def test_hello1(self):
        self.setUpBrowser('firefox')
        driver = self.driver
        driver.get(self.launch_url)
        self.assertIn("Google", driver.title)
        if driver.find_element(By.CSS_SELECTOR, "img#hplogo") is None:
            #----
            pass
        #self.assertEqual(1, 0, "broken")
#        driver.close()

    def test_hello2(self):
        self.setUpBrowser('ie')
        driver = self.driver
        driver.get(self.launch_url)
        self.assertIn("Google", driver.title)
        if driver.find_element(By.CSS_SELECTOR, "img#hplogo") is None:
            #----
            pass
        #self.assertEqual(1, 0, "broken")
#        driver.close()


    def tearDown(self):
        self.driver.close()
        #if self.driver:
        #    self.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()

