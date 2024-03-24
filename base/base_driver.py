from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
            page_len = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var page_len=document.body.scrollHeight;return page_len;")
            match = False

            while (match == False):
                lastCount = page_len
                sleep(1)
                page_len = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var page_len=document.body.scrollHeight;return page_len;")
                if lastCount == page_len:
                    match = True
            if match == True:
                sleep(2)
                self.driver.execute_script("window.scrollTo(0, 0);")
            sleep(4)

    def check_all_elements_presence(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 60)  # for explicit waits
        return wait.until(
            EC.presence_of_all_elements_located(
                (
                    locator_type,
                    locator
                )
            )
        )
    
    def check_if_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 60)  # for explicit waits
        return wait.until(
            EC.element_to_be_clickable(
                (locator_type, locator)
            )
        )
