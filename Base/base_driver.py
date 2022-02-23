import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Put methods here that can be use by the different pages or can be inherited by the class
# Do not forget to declare the Super () class in every page that will inherit this BaseDriver class

class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    # Contains generic method that can be usable in all pages
    # Externalize all the method using "wait" and create a method on the BASE package
    # Create a generic method for each EC (presence of element, clickable, url contains etc)

    def wait_contains_url(self, locator):
        wait = WebDriverWait(self.driver, 30)
        url_page = wait.until(EC.url_contains(locator))
        return url_page

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    # def page_scroll(self):
    #     # This will scroll the page down
    #     self.driver.execute_script("window.scrollTo(0,400)")
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0,600)")
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0,800)")
    #     time.sleep(2)