# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Record01102041424Pm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_record01102041424_pm(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1366,576 | ]]
        driver.maximize_window()
        driver.get("https://test2-pg.cailian.net/#/login")
        # ERROR: Caught exception [ERROR: Unsupported command [openWindow |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]

        time.sleep(3)
        # driver.find_element_by_css_selector("input.el-input__inner").clear()
        # driver.find_element_by_css_selector("input.el-input__inner").send_keys("")
        driver.find_element_by_css_selector("input.el-input__inner").clear()
        driver.find_element_by_css_selector("input.el-input__inner").send_keys("18610933265")
        time.sleep(3)
        driver.find_element_by_css_selector("div.zlpg-login").click()

        driver.find_element_by_css_selector("div.inputPassword.el-input > input.el-input__inner").clear()
        driver.find_element_by_css_selector("div.inputPassword.el-input > input.el-input__inner").send_keys("222222")
        driver.find_element_by_css_selector("div.kaptchaCode.fl.el-input > input.el-input__inner").click()
        driver.find_element_by_css_selector("div.kaptchaCode.fl.el-input > input.el-input__inner").clear()
        driver.find_element_by_css_selector("div.kaptchaCode.fl.el-input > input.el-input__inner").send_keys("1111")

        driver.find_element_by_css_selector("div.submit-btn").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.el-radio__inner").click()

        driver.find_element_by_link_text(u"确定").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"快速创建项目").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.el-input.el-input--mini > input.el-input__inner").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.el-input.el-input--mini > input.el-input__inner").clear()
        time.sleep(3)
        driver.find_element_by_css_selector("div.el-input.el-input--mini > input.el-input__inner").send_keys("44")
        time.sleep(3)
        driver.find_element_by_css_selector(
            "div.el-input.el-input--mini.el-input--suffix > input.el-input__inner").click()
        time.sleep(3)
        driver.find_element_by_css_selector("li.el-select-dropdown__item.hover").click()
        / html / body / div[3] / div[1] / div[1] / ul / li[7] / span[contains(text(), '房地产估值报')]
        driver.find_element_by_xpath(/ html / body / div[3] / div[1] / div[1] / ul / li[7] / span[contains(text(), '房地产估值报')])
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[3]/div[1]/div[1]/ul/li[1]").click()

        time.sleep(3)
        driver.find_element_by_css_selector("div.pv.el-input.el-input--mini > input.el-input__inner").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.pv.el-input.el-input--mini > input.el-input__inner").clear()
        time.sleep(3)
        driver.find_element_by_css_selector("div.pv.el-input.el-input--mini > input.el-input__inner").send_keys("44")
        time.sleep(3)
        driver.find_element_by_css_selector(
            "div.el-date-editor.assessmentBaseDate.el-input.el-input--mini.el-input--prefix.el-input--suffix.el-date-editor--date > input.el-input__inner").click()
        driver.find_element_by_css_selector("td.available.today > div > span").click()
        time.sleep(3)
        driver.find_element_by_css_selector("body.el-loading-parent--relative.el-loading-parent--hidden").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//div[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div").click()
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.center-body").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div/div[3]/div").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//div[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[5]/div").click()
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.input.frist-tr.text-left.bgColor").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.input.frist-tr.text-left.bgColor").clear()
        time.sleep(3)
        driver.find_element_by_css_selector("input.input.frist-tr.text-left.bgColor").send_keys("55")
        time.sleep(3)
        driver.find_element_by_css_selector("button.el-button.saveBtn.fs13.el-button--primary > span").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.search-btn").click()
        time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
