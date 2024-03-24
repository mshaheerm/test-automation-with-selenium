from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchResults(BaseDriver):
    log = Utils.add_logs()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    NO_STOP_FILTER_BUTTON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    ONE_STOP_FILTER_BUTTON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    TWO_STOPS_FILTER_BUTTON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    SEARCH_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    # Get all the elements located
    def get_no_stop_button_element(self):
        return self.driver.find_element(By.XPATH, self.NO_STOP_FILTER_BUTTON)

    def get_single_stop_button_element(self):
        # return self.driver.find_element(By.XPATH, self.ONE_STOP_FILTER_BUTTON)
        return self.check_if_element_is_clickable(By.XPATH, self.ONE_STOP_FILTER_BUTTON)
    
    def get_double_stop_button_element(self):
        return self.driver.find_element(By.XPATH, self.TWO_STOPS_FILTER_BUTTON)

    def get_search_flight_results_elements(self):
        return self.check_all_elements_presence(By.XPATH, self.SEARCH_RESULTS)

    # Set values/click on located elements
    def click_no_stop_button_element(self):
        self.get_no_stop_button_element().click()

    def click_single_stop_button_element(self):
        sleep(2)
        self.get_single_stop_button_element().click()

    def click_double_stop_button_element(self):
        self.get_double_stop_button_element().click()

    def filter_by_stops(self, num_stops):
        if num_stops == "Non Stop":
            self.log.info("Direct Flights")
            # sleep(1)
            self.click_no_stop_button_element()
        elif num_stops == "1 Stop":
            self.log.info("Flights with 1 stop")
            sleep(2)
            self.click_single_stop_button_element()
        elif num_stops == "2 Stop":
            self.log.info("Flights with 2 stops")
            # sleep(2)
            self.click_double_stop_button_element()
        else:
            self.log.WARNING("Invalid Selection!!!")
