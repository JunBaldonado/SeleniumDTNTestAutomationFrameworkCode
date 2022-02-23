import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

# BaseDriver class was invoke in this class and the Super init is very important
# BaseDriver was invoke in the class so that we can use whatever method we have on the Base Directory
# We don't have the self.wait initialize because we did not use it in this page

class Dashboard(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NEWS_MENU_FIELD = "//a[contains(@class,'navMenu-item-link js-tab-anchor')][normalize-space()='News']"
    NEWS_OPTION_FIELD = "//a[contains(@class,'navMenu-subList-item-link')][normalize-space()='AP Online']"
    NEWS_ARTICLE_FRAME = "//li[@class='featureList-item featureList-item_arrow isActive']//a[@class='featureList-item-link featureList-item-link_narrow js-external-news-headline-item']"
    NEWS_PAGE_ELEMENT = "//li[contains(@class,'featureList-item featureList-item_arrow isActive')]"

    # Create method to assign the variables
    def get_news_menu_field(self):
        return self.driver.find_element(By.XPATH, self.NEWS_MENU_FIELD)

    def get_news_option_field(self):
        return self.driver.find_element(By.XPATH, self.NEWS_OPTION_FIELD)

    def get_news_article_frame(self):
        return self.driver.find_element(By.XPATH, self.NEWS_ARTICLE_FRAME)

    def get_news_element(self):
        return self.driver.find_element(By.XPATH, self.NEWS_PAGE_ELEMENT)

    def hover_news_menu(self):
        news = self.get_news_menu_field()
        achains = ActionChains(self.driver)
        achains.move_to_element(news).perform()

    def click_news_option(self):
        self.get_news_option_field().click()
        f1 = self.get_news_article_frame()
        achains1 = ActionChains(self.driver)
        achains1.move_to_element(f1).click().send_keys(Keys.END).perform()


    # Create method for the ACTION of the locator
    # created method that is seen in this page, POM concept
    # def news_menu(self):
    #     # Mouse over the NEWS menu
    #     news = self.driver.find_element(By.XPATH,
    #                                     "//a[contains(@class,'navMenu-item-link js-tab-anchor')][normalize-space()='News']")
    #     achains = ActionChains(self.driver)
    #     achains.move_to_element(news).perform()
    #
    # # created method that is seen in this page, POM concept
    # def click_ap_online(self):
    #     # Click on the ApOnline option
    #     self.driver.find_element(By.XPATH,
    #                              "//a[contains(@class,'navMenu-subList-item-link')][normalize-space()='AP Online']").click()
    #     f1 = self.driver.find_element(By.XPATH,
    #                                   "//li[@class='featureList-item featureList-item_arrow isActive']//a[@class='featureList-item-link featureList-item-link_narrow js-external-news-headline-item']")
    #     achains1 = ActionChains(self.driver)
    #     achains1.move_to_element(f1).click().send_keys(Keys.END).perform()
    #     time.sleep(5)
