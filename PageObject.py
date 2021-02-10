from Selectors import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# each Class encapsulates method implementations of all action-step on a specific page
# each Method in a class represents a single action-step on that page
class HomePage():
    def searchTerm(self, term):
        elem = self.driver.find_element_by_css_selector(CSS_HOMEPAGE_SEARCH)
        elem.clear()
        elem.send_keys(term)
        elem.submit()

    def precenceOfLogo(self):
        self.assertTrue(len(self.driver.find_elements_by_css_selector(CSS_HOMEPAGE_LOGO)) > 0)


class SearchResults():
    def filterByThisWeek(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SEARCHRESULTS_FILTER))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH_SEARCHRESULTS_FILTER_THISWEEK))).click()
        WebDriverWait(self.driver, 5).until_not(EC.visibility_of_element_located((By.XPATH, XPATH_SEARCHRESULTS_FILTER_THISWEEK)))

    def checkDatesAreThisWeek(self):
        video_dates = self.driver.find_elements_by_xpath(XPATH_SEARCHRESULTS_VIDEO_DATES)
        self.assertTrue("month" not in video_dates[0].text)
        self.assertTrue("month" not in video_dates[1].text)

    def filterByChannel(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SEARCHRESULTS_FILTER))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, XPATH_SEARCHRESULTS_FILTER_CHANNEL))).click()
        WebDriverWait(self.driver, 5).until_not(
            EC.visibility_of_element_located((By.XPATH, XPATH_SEARCHRESULTS_FILTER_CHANNEL)))

    def checkChannelsDisplayed(self):
        elems = self.driver.find_elements_by_xpath(XPATH_SEARCHRESULTS_BUTTON_SUBSCRIBE)
        self.assertTrue(len(elems) > 10)

    def clickOnNthVideo(self,n):
        self.assertTrue(n > 0, "parameter must be positive number")
        elems = self.driver.find_elements_by_xpath(XPATH_SEARCHRESULTS_VIDEO_TITLE)
        elems[n-1].click()

class VideoPlay():
    def play(self):
        self.driver.find_element_by_xpath(XPATH_VIDEOPAGE_BUTTON_PLAY).click()

    def pause(self):
        self.driver.find_element_by_xpath(XPATH_VIDEOPAGE_BUTTON_PAUSE).click()

    def isPlaying(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, XPATH_VIDEOPAGE_BUTTON_PAUSE)))

    def isPaused(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, XPATH_VIDEOPAGE_BUTTON_PLAY)))

