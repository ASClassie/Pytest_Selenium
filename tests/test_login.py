import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, json
from pages.loginpage import LoginPage
from utilities.config_reader import get_base_url
import allure


'''Locators'''

Validation_ERROR_locator = "//p[text()='Your email or password is incorrect!']"
VALIDATION_ERR = "Your email or password is incorrect!"


def user_data():
    file_path = os.path.join(os.path.dirname(__file__), "../Data/user_credentials.json")
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path,exist_ok=True)
    with open(file_path, 'r') as file:
        return json.load(file)


def invalid_user():
    user = user_data()
    return user[1:]



@allure.feature("Login Module")
class TestLogin:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self,driver, valid_user,login):
        """
                Scenario: Valid login with correct credentials
                Given: User is on login page
                When: User enters correct email and password
                Then: User is redirected to home page
                """

        with allure.step("Navigate to login page"):
            login.navigate_to(get_base_url() + "/login")
            login.logger.info("Navigated to base URL")
            login.take_screenshot("Login Page")



        with allure.step("Enter valid credentials and submit"):
            login.login_as(valid_user['username'], valid_user['password'])
            login.logger.info("Submitted login form")
            login.take_screenshot("After Login Submit")


        with allure.step("Verify home page loaded"):
            login.wait.until(EC.title_contains("Automation Exercise"))
            login.take_screenshot("Homepage")


    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("users", invalid_user())
    def test_invalid_login(self,driver,login,users):
        """
                Scenario: Invalid login with wrong credentials
                Given: User is on login page
                When: User enters incorrect email or password
                Then: Validation message is displayed
                """

        with allure.step("Navigate to login page"):
            login.navigate_to(get_base_url() + "/login")
            login.logger.info("Navigated to base URL")
            login.take_screenshot("Invalid Login Page")

        with allure.step("Enter invalid credentials and submit"):
            login.login_as(users['username'], users['password'])
            login.logger.info("Submitted invalid login form")
            login.take_screenshot("After Invalid Login Submit")

        with allure.step("Validate error message"):
            validation_error = login.wait.until(
                EC.visibility_of_element_located((By.XPATH, Validation_ERROR_locator))
            )
            assert validation_error.text.strip() == VALIDATION_ERR
            login.take_screenshot("Validation Error Displayed")










