from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver) # Calling the BasePage constructor
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[text()='Login']")

    def enter_username(self, username):
        self.find_element(self.username_field).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.password_field).send_keys(password)

    def click_login(self):
        self.find_element(self.login_button).click()
        from pages.home_page import HomePage  # Import here to avoid circular imports
        return HomePage(self.driver)

    def login_as(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()
