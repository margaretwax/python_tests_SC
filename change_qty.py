# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from helper import do_login

import unittest, time

class Change_qty(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.base_url = "https://qa.solidcommerce.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_123(self):
        driver = self.driver
        driver.get(self.base_url + "/login.aspx?redirectOnSuccess=/Pages/Inventory/InventoryManager.aspx")


        find_id = driver.find_element_by_id
        find_xpath = driver.find_element_by_xpath

        do_login(self.driver)

        #driver.find_element_by_css_selector("span.rmText.rmExpandDown").click()
        find_xpath(".//*[@id='ctl00_menuTop']/ul/li[2]/a/span").click()
        find_xpath(".//*[@id='ctl00_menuTop']/ul/li[2]/div/ul/li[7]/a/span").click()

    #driver.find_element_by_css_selector("a.rmLink.rmFocused > span.rmText").click()
        #driver.find_element_by_css_selector("span.rtPlus.rtPlusHover").click()

        #sleep for 2 sec
        time.sleep(2)

        #expand Marketplaces
        find_xpath(".//*[@id='ctl00_ContentPlaceHolder1_tvInventory']/ul/li[3]/div/span[2]").click()

        time.sleep(2)

        #ebay
        find_xpath(".//*[@id='ctl00_ContentPlaceHolder1_tvInventory']/ul/li[3]/ul/li[4]/div/span[2]").click()

        time.sleep(2)

        #click on TestMS list
        find_xpath(".//*[@id='ctl00_ContentPlaceHolder1_tvInventory']/ul/li[3]/ul/li[4]/ul/li[44]/div/span[2]").click()

        time.sleep(2)

        #click on 'search' button
        find_xpath(".//*[@id='ctl00_ContentPlaceHolder1_Search1_bSearchProductsUserControl']").click()

        time.sleep(2)

        #driver.find_element_by_id("ctl00_ContentPlaceHolder1_Search1_bSearchProductsUserControl").click()

        time.sleep(2)
        #Change qty
        find_id("tbQtyFormula").clear()
        find_id("tbQtyFormula").send_keys("2")
        time.sleep(2)
        find_id("ctl00_ContentPlaceHolder1_bSave").click()
        time.sleep(2)

        #log out
        find_id("ctl00_lbLogOut").click()
        time.sleep(2)

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
