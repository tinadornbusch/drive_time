from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from time import sleep

GOOGLE_MAPS = "https://www.google.com/maps"
SLEEP_TIME = 3


class DrivingDistanceCalc:
    """Using Google Maps, calculates current minimum drive time between two zip codes.
    If it encounters an error, will return 999999"""
    def __init__(self):
        # Set up webdriver and pull up Google Maps webpage
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(GOOGLE_MAPS)

    def calc_drive_time(self,start,destination):
        # Search destination zip code in Google Maps
        search_bar = self.driver.find_element(by="id", value="searchboxinput")
        search_bar.send_keys(f"{destination}, USA")
        search_bar.send_keys(Keys.ENTER)
        sleep(SLEEP_TIME)

        # Click button to get directions to destination zip code
        try:
            directions_button = self.driver.find_element(by="class name", value="g88MCb")
        except selenium.common.exceptions.NoSuchElementException:
            time_num = "999999"
        else:
            directions_button.click()
            sleep(SLEEP_TIME)

            # Search origin zip code and hit enter to find directions
            origin_search = self.driver.find_element(by="class name", value="tactile-searchbox-input")
            origin_search.send_keys(f"{start}, USA")
            origin_search.send_keys(Keys.ENTER)
            sleep(SLEEP_TIME)

            # Extract string representing estimated drive time between the two locations
            try:
                time_num = self.driver.find_element(by="css selector", value=".XdKEzd div").text
            except selenium.common.exceptions.NoSuchElementException:
                time_num = "999999"
            else:
                pass

        self.driver.close()
        return time_num
