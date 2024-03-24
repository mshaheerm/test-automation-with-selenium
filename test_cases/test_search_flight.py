import pytest
import softest
from time import sleep
from utilities.utils import Utils
from pages.yatra_index_uae import UAEIndexPage
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchandVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setups(self):
        self.uae_index_page = UAEIndexPage(self.driver)
        self.utils = Utils()


    # @file_data("../test_data/data.json")  # provide data from a json or yaml file
    # @data(*Utils.read_data_from_excel("./test_data/xl_data.xlsx", "Sheet1"))  # provide data from an excel sheet
    @data(*Utils.read_data_from_csv("./test_data/data.csv"))  # provide data from a csv file
    @unpack
    def test_search_flights(
        self,
        source,
        destination,
        date,
        num_stops
    ):
        yatra_home = self.uae_index_page.goto_yatra_india()
        search_results = yatra_home.search_flights(source, destination, date)
        yatra_home.page_scroll()  # Scroll to end
        sleep(2)
        search_results.filter_by_stops(num_stops)  # Select 1 stop
        flights = search_results.get_search_flight_results_elements()
        self.utils.assert_text(flights, num_stops)  # check if the search result is correct
