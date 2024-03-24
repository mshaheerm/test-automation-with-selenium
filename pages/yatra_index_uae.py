from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from pages.yatra_index import IndexPage


class UAEIndexPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    YATRA_IND = "//a[normalize-space()='Yatra.com']"

    # Get all the elements located    
    def get_yatra_india_button_element(self):
        return self.driver.find_element(By.XPATH, self.YATRA_IND)

    # Set values/click on located elements
    def click_yatra_india_website_element(self):
        self.get_yatra_india_button_element().click()
    
    def goto_yatra_india(self):
        self.click_yatra_india_website_element()  # goto yatra.com india
        index_page = IndexPage(self.driver)
        return index_page
