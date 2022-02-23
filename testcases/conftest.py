import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Conftest contains the setup and tierdown method
# The driver and wait variable was introduce here and will instantiated in the other pages
# Fixture is declared in this package and the scope was class so that every class can use it
# In order to call this fixture we need request to give access to the class that will use driver or wait
# cls means class in the request.

@pytest.fixture(scope="class")
def setup(request, browser,): # Add the url if you want to have the url link in the command line included
        if browser == "chrome":
        # driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # elif browser == "firefox":
            # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # driver.get("https://pre-www.mydtn.com/agriculture/web/ag/login") # change to driver.get(url)
            driver.maximize_window()
            driver.get("https://pre-www.mydtn.com/agriculture/web/ag/login")
            wait = WebDriverWait(driver, 30)
            wait.until(EC.url_contains("https://pre-www.mydtn.com/agriculture/web/ag/login"))
            request.cls.driver = driver
            yield
            driver.close()



def pytest_addoption(parser):
        parser.addoption("--browser")
        # If you want to add a url
        # parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
        return request.config.getoption("--browser")


# Then add another fixture for the url
# @pytest.fixture(scope="class", autouse=True)
# def url(request):
#     return request.config.getoption("--url")

    # driver_service = Service(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    # wait = WebDriverWait(driver, 10)
    # driver.get("https://pre-www.mydtn.com/agriculture/web/ag/login")
    # driver.maximize_window()
    # calling the variable in the fixture by request
    # request.cls.driver = driver
    # request.cls.wait = wait
    # yield
    # driver.close()


