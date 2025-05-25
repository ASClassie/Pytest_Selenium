import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("HomePage Module")
class TestHomePage:
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    CONTACT_US_BTN = (By.XPATH, "//a[contains(text(),'Contact us')]")
    PRODUCTS_BTN = (By.XPATH, "//a[contains(text(),'Products')]")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout')]")
    CART_BTN = (By.XPATH, "//a[contains(text(),'Cart')]")
    USERNAME_DISPLAY = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    @allure.story("Adding Products")
    @allure.severity(allure.severity_level.NORMAL)
    def test_adding_multiple_products(self,driver,logged_in_user):
        """
                            Scenario: Adding products to the cart
                            Given: User is on Homepage
                            When: User clicks on the Products option on the top navigation bar
                            And : User is redirected to the Products page
                            And : User adds multiple products by clicking on the Add to Cart button
                            Then: User should get a success message for each product adding in cart
                            """
        with allure.step("User clicks on the products link on the Homepage"):
            logged_in_user.click_products()
            logged_in_user.take_screenshot("Products page is opened")

        with allure.step("User adds multiple products to the cart"):
            action = ActionChains(driver)
            product_cards = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")

            for card in product_cards:
                driver.execute_script("arguments[0].scrollIntoView(true);",card)
                time.sleep(1)
                action.move_to_element(card).perform()
                time.sleep(1)
                add_button = card.find_element(By.XPATH,".//div[@class='product-overlay']//a[text()='Add to cart']")
                add_button.click()
                logged_in_user.take_screenshot("adding product")
                # Handle modal (continue shopping)
                continue_btn = logged_in_user.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']")))
                continue_btn.click()
            logged_in_user.click_cart()










