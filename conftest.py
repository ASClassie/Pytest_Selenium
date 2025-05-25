import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
from tests.test_login import user_data
from utilities.config_reader import get_base_url

# Custom command-line options
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Type in browser name (chrome/firefox/edge)")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


def create_driver(browser_name,headless):
    driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    return driver


# Driver fixture for single-browser tests
@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')
    driver = create_driver(browser_name,headless)
    yield driver
    driver.quit()

# Driver fixture for multi-browser tests
@pytest.fixture(params=["chrome", "firefox", "edge"])
def multi_(request):
    browser_name =request.param
    headless = request.config.getoption('--headless')
    driver = create_driver(browser_name, headless)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    from pages.loginpage import LoginPage
    return LoginPage(driver)

@pytest.fixture
def valid_user():
    user = user_data()
    return user[0]

@pytest.fixture
def logged_in_user(driver,valid_user,login):
    login.navigate_to(get_base_url() + "/login")
    homepage = login.login_as(valid_user['username'], valid_user['password'])
    return homepage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Lazy import inside function
            from pages.base_page import BasePage
            base = BasePage(driver)
            base.take_screenshot(step_name="failure")

