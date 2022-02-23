import time

import pytest
import softest

from pages.mydtn_login_page import LoginPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack

# Whoever will use this fixture should add @pytest.mark.usefixtures("setup")
# "setup" being the name of the function we created, this will pass to the class that will use the fixture
# In order to use the fixture in the conftest file we need to declare it as @pytest.mark.usefixtures(NAMEofFIXTURE)


@pytest.mark.usefixtures("setup")
@ddt
class TestSelectNews(softest.TestCase):

    # We want to externalize all class object in this test case so we will create the class_setup method
    @pytest.fixture(autouse=True)
    # Externalize the variables use in this page
    def class_setup(self):
        self.sa = LoginPage(self.driver)
        self.ut = Utils()

    # @data(("josejr_PREMYDTN", "josbal@2021")) #, ("Aju.jayapalan", "Agile123")
    # @unpack
    # @file_data("../testdata/testdata.json")
    @file_data("../testdata/testyml.yaml")
    def testselect_news(self, username, password):
        # Launching browser and opening the MyDTN, this is in the conftest fixtures

        # Resolve any sync issue
        # Login to myDTN (username, password, url) , always create an object of the class (sa) for the page
        # sa = LoginPage(self.driver)
        # self.sa.wait_contains_url("https://pre-www.mydtn.com/agriculture/web/ag/login")
        # Use the created class object (news_menu) in the mydtn_login that link mydtn_dashboard
        time.sleep(10)
        login_news_link = self.sa.log_to_url(username, password)

        # Mouse over the NEWS menu, always create an object of the class (nm) for the page
        # nm = Dashboard(self.driver)
        login_news_link.hover_news_menu()

        # Click on the AP Online option
        login_news_link.click_news_option()

        # assertion example that will be contained in the utilities
        f2 = login_news_link.get_news_element()
        # ut = Utils()
        self.ut.assertItemText(f2, "AgOnline")

        # This will scroll the page down, this is part of the Base --- BaseDriver class
        # We can use the object of the class (nm) since we have instantiated the BaseDriver in the class Dashboard
        # nm.page_scroll()


