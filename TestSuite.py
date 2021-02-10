import unittest
from PageObject import * # importing PageObject makes methods of all classes avalable here


class TestSuite_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)

    # highly abstract test cases start here
    #  easy to implement
    #  easily extensible
    #  no object creation, no dynamic memory usage, using static calls
    # pointer "self" of this class is pass to each methods, making self.driver accessible in PageObject
    def test_SearchFilterThisWeek(self):
        HomePage.precenceOfLogo(self)
        HomePage.searchTerm(self, SEARCH_TERM_AUTOMATION)
        SearchResults.filterByThisWeek(self)
        SearchResults.checkDatesAreThisWeek(self)

    def test_LookForChannelsOnly(self):
        HomePage.searchTerm(self, SEARCH_TERM_AUTOMATION)
        SearchResults.filterByChannel(self)
        SearchResults.checkChannelsDisplayed(self)

    def test_SearchAndPlayVideo(self):
        HomePage.searchTerm(self, SEARCH_TERM_MANUAL)
        SearchResults.clickOnNthVideo(self,2)
        VideoPlay.isPlaying(self)

    def test_PlayPauseFunctionality(self):
        HomePage.searchTerm(self, SEARCH_TERM_MANUAL)
        SearchResults.clickOnNthVideo(self,2)
        VideoPlay.isPlaying(self)
        VideoPlay.pause(self)
        VideoPlay.isPaused(self)
        VideoPlay.play(self)
        VideoPlay.isPlaying(self)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
