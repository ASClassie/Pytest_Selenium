from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def __init__(self, driver:WebDriver):
        super().__init__(driver) # Calling the BasePage constructor
    # Locators
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    CONTACT_US_BTN = (By.XPATH, "//a[contains(text(),'Contact us')]")
    PRODUCTS_BTN = (By.XPATH, "//a[contains(text(),'Products')]")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout')]")
    CART_BTN = (By.XPATH, "//a[contains(text(),'Cart')]")
    USERNAME_DISPLAY = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    # Actions
    def click_signup_login(self):
        self.find_element(self.SIGNUP_LOGIN_BTN).click()

    def click_contact_us(self):
        self.find_element(self.CONTACT_US_BTN).click()

    def click_products(self):
        element = self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_BTN))
        element.click()
        self.wait.until(EC.title_contains("Automation Exercise - All Products"))

    def click_logout(self):
        self.find_element(self.LOGOUT_BTN).click()

    def click_cart(self):
        self.find_element(self.CART_BTN).click()

    def get_logged_in_username(self):
        return self.get_text(self.USERNAME_DISPLAY).text