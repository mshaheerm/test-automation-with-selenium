from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from pages.search_flights_result import SearchResults
from utilities.utils import Utils


class IndexPage(BaseDriver):
    log = Utils.add_logs()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    ARRIVE_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    ARRIVE_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    DEPARTURE_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"
    POPUP_CLOSE_BUTTON_X_OFFSET = 24
    POPUP_CLOSE_BUTTON_Y_OFFSET = 24

    # Get elements
    def get_depart_from_field_element(self):
        return self.check_if_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_arrive_to_field_element(self):
        return self.check_if_element_is_clickable(By.XPATH, self.ARRIVE_TO_FIELD)
    
    def get_arrive_to_field_elements_list(self):
        return self.check_all_elements_presence(By.XPATH, self.ARRIVE_TO_RESULT_LIST)

    def get_departure_date_field_element(self):
        return self.check_if_element_is_clickable(By.XPATH, self.DEPARTURE_DATE_FIELD)
    
    def get_departure_date_field_elements_list(self):
        return self.check_if_element_is_clickable(By.XPATH, self.ALL_DATES)
    
    def get_search_button_element(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    # Set values/click on located elements
    def click_close_button_element(self):
        sleep(6)
        actions = ActionChains(self.driver)
        actions.move_by_offset(24, 24).perform()
        actions.click()
        self.log.info("Closing popup window")

    def set_depart_from_field_element_value(self, departure_from):
        self.log.info("locating depart-from element and clicking it.")
        self.get_depart_from_field_element().click()
        self.log.info("Clicked depart from successfully.")
        self.log.info("Writing source airport name.")
        self.get_depart_from_field_element().send_keys(departure_from)
        self.log.info("Source airport name written successfully.")
        self.log.info("Selecting Source airport name..")
        self.get_depart_from_field_element().send_keys(Keys.ENTER)
        self.log.info("Source airport name selected successfully.")
    
    def set_arrive_to_field_element_value(self, arrival_to):
        self.log.info("locating arrive-to element and clicking it.")
        self.get_arrive_to_field_element().click()
        self.log.info("Clicked arrive-to successfully.")
        self.log.info("Writing destination airport name.")
        self.get_arrive_to_field_element().send_keys(arrival_to)
        sleep(2)
        self.log.info("Destination airport name written successfully.")
        self.log.info("Selecting Destination airport name from the list.")
        search_results = self.get_arrive_to_field_elements_list()
        sleep(2)
        for result in search_results:
            if arrival_to in result.text:
                result.click()
                break
        self.log.info("Destination airport name selected successfully.")

    def set_departure_date_field_element_value(self, departure_date):
        sleep(3)
        self.log.info("locating departure-date element and clicking it.")
        self.get_departure_date_field_element().click()
        self.log.info("Clicked departure-date successfully.")
        self.log.info("Selecting departure-date from the list.")
        all_dates = self.get_departure_date_field_elements_list().find_elements(
            By.XPATH,
            self.ALL_DATES
        )
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                break
        self.log.info("Departure date selected successfully.")
        
    def click_search_flights_button(self):
        self.log.info("locating search button element and clicking it.")
        self.get_search_button_element().click()
        self.log.info("Clicked searched button successfully.")

    def search_flights(self, source, destination, departure_date):
        # self.get_close_button_element()
        self.click_close_button_element()
        self.set_depart_from_field_element_value(source)  # Provide going from location
        # sleep(3)
        self.set_arrive_to_field_element_value(destination)  # Provide going to location
        self.set_departure_date_field_element_value(departure_date)  # Provide travelling date
        self.click_search_flights_button()  # Start searching
        search_flight_results = SearchResults(self.driver)
        return search_flight_results
