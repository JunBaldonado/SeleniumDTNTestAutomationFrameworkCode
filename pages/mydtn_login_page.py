import time

from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from pages.mydtn_dashboard import Dashboard
# BaseDriver class was invoke in this class and the Super init is very important
# BaseDriver was invoke in the class so that we can use whatever method we have on the Base Directory
# def __init__ is essential in order that we declare all variables that will be called in the pages

class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # Locators
    # Pass the web element to a variable
    USERNAME_FIELD = "_58_login"
    PASSWORD_FIELD = "_58_password"
    CLICK_BUTTON = "signIn-button"

    # Method to get the locators and return it to the variable
    def get_user_path_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.USERNAME_FIELD)

    def get_password_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PASSWORD_FIELD)

    def get_sign_in_button(self):
        return self.driver.find_element(By.CLASS_NAME, self.CLICK_BUTTON)

    # Method for the ACTION of the locators
    def enter_user(self, username):
        time.sleep(5)
        self.get_user_path_field().send_keys(username)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_sign_in(self):
        self.get_sign_in_button().click()

    def log_to_url(self, username, password):
        self.enter_user(username)
        self.enter_password(password)
        self.click_sign_in()

    # create an object of the class, in order to link the two page mydtn_login and mydtn_dashboard
        login_news_link = Dashboard(self.driver)
        return login_news_link

    # created method that is seen in the mydtnlogin page, POM concept
    # def pwd(self, password):
    #     pd = self.wait_until_element_is_clickable(By.NAME, )
    #     pd.send_keys(password)

    # created method that is seen in the mydtnlogin page, POM concept
    # def click_sign_in(self):
    #     self.driver.find_element(By.CLASS_NAME, "signIn-button").click()