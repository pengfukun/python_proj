# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     base_pfk
# Author:      Pengfukun
# Datetime:    2021/5/18 17:06
# Description：
# -----------------------------------------------------------------------------------
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, browser):
        if browser == "Chrome" or browser == "c" or browser == "C":
            self.driver = webdriver.Chrome()  # 实例化谷歌浏览器
        elif browser == "Firefox" or "f" or "F":
            self.driver = webdriver.Firefox()  # 实例化火狐浏览器
        else:
            raise NameError("请输入正确的浏览器")
        self.driver.maximize_window()  # 最大化窗口
        self.driver.get("http://127.0.0.1/ranzhi=/sys/user-login.html")  # 打开网页
        self.driver.implicitly_wait(20)  # 隐式等待

    def selector_to_locator(self, selector):
        """
        获取定位方法
        :param selector:
        :return:
        """
        selector_by = selector.split(",")[0].strip()  # 定位方法
        selector_value = selector.split(",")[1].strip()  # 值
        if selector_by == "i" or selector_by == "id":
            locator = (By.ID, selector_value)
        elif selector_by == "x" or selector_by == "xpath":
            locator = (By.XPATH, selector_value)
        elif selector_by == "n" or selector_value == "name":
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == "class":
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "s" or selector_by == "css":
            locator = (By.CSS_SELECTOR, selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            locator = (By.LINK_TEXT,selector_value)
        elif selector_by == "p" or selector_by == "part_link_text":
            locator = (By.PARTIAL_LINK_TEXT,selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            locator = (By.TAG_NAME, selector_value)
        else:
            raise NameError("请输入正确的定位方法")
        return locator

    def locator_element(self, selector):
        """
        定位元素
        :param selector:
        :return:
        """
        locator = self.selector_to_locator(selector)
        #隐式等待
        return WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located(locator))
        # return self.driver.find_element(*locator)

    def click(self, selector):
        """
        D点击元素
        :return:
        """
        self.locator_element(selector).click()

    def send_key(self, selector, text):
        """
        输入内容
        :param selector:
        :return:
        """
        ele=self.locator_element(selector)
        ele.clear()
        ele.send_keys(text)

    def swtich_to_iframe(self, selector):
        """
        进入框架
        :param selector:
        :return:
        """
        ele = self.locator_element(selector)
        self.driver.switch_to.frame(ele)

    def locator2(self, selector, selector2):
        """
        二次定位
        :param selector:
        :param selector2:
        :return:
        """
        loc = self.selector_to_locator(selector)
        loc2 = self.selector_to_locator(selector2)
        ele = self.driver.find_element(*loc).find_elements(*loc2)
        random.choice(ele).click()


    def sleepandquit(self):
        """
        退出
        :return:
        """
        sleep(2)
        self.driver.quit()
    def get_text(self,selector):
        """
        获取文本
        :param selector:
        :return:
        """
        return self.locator_element(selector).text
    def get_screenshot(self,filename):
        """
        截图
        :param filename:
        :return:
        """
        self.driver.get_screenshot_as_file(filename)