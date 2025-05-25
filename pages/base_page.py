from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utilities.logger_util import *
import os
from datetime import datetime
import allure
import inspect
from selenium.webdriver.remote.webdriver import WebDriver
"""
BasePage: Core class for reusable Selenium actions.
Usage:
- Inherit this class in all Page Object classes
- Use methods like `click()`, `clear_and_send_keys()` etc. for stable test runs
"""

class BasePage:
    """Base class for all page objects"""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.logger = TestLogger()

    def navigate_to(self, url):
        """Navigate to the given URL"""
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def get_title(self):
        """Get the page title"""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL"""
        return self.driver.current_url

    def find_element(self, locator):
        """Find element by locator"""
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            self.logger.error(f"Element not found with locator: {locator}")
            raise e

    def find_elements(self, locator):
        """Find elements by locator"""
        return self.driver.find_elements(*locator)

    def is_element_present(self, locator):
        """Check if element is present"""
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            self.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            self.logger.error(f"Element not visible within {timeout} seconds: {locator}")
            raise e

    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait for element to be clickable"""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            self.logger.error(f"Element not clickable within {timeout} seconds: {locator}")
            raise e

    def wait_for_element_presence(self, locator, timeout=10):
        """Wait for element to be present in DOM"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            self.logger.error(f"Element not present within {timeout} seconds: {locator}")
            raise e

    def clear_and_send_keys(self, locator, text):
        """Clear the field and send keys"""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """Click on element"""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def js_click(self,locator):
        element = self.wait_for_element_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def take_screenshot(self, step_name="screenshot"):
        """Capture screenshot with dynamic test name and step, save to test_results/screenshots, attach to Allure"""

        # ✅ Get the test function name dynamically from the call stack
        test_name = inspect.stack()[1].function

        # ✅ Timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # ✅ Create filename: testname_stepname_timestamp.png
        filename = f"{test_name}_{step_name}_{timestamp}.png"

        # ✅ Save to desired directory
        base_dir = "D:\\Pytest_Selenium"
        screenshot_folder = os.path.join(base_dir, "test-results", "screenshots")
        os.makedirs(screenshot_folder, exist_ok=True)
        full_path = os.path.join(screenshot_folder, filename)

        # ✅ Save screenshot
        self.driver.save_screenshot(full_path)

        # ✅ Attach to Allure
        allure.attach.file(full_path, name=step_name, attachment_type=allure.attachment_type.PNG)

        # ✅ Optional logger
        self.logger.info(f"Screenshot saved and attached: {full_path}")

        return full_path