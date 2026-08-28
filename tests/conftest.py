import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv

from pages.registration_page import RegistrationPage
from utils import attach

load_dotenv()
selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASSWORD")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope="function")
def driver(request):
    # Получаем все параметры
    use_selenoid = request.config.getoption("--selenoid", default=False)
    browser = request.config.getoption("--browser", default="chrome")
    browser_version = request.config.getoption("--browser_version", default="154.0")
    headless = request.config.getoption("--headless", default=False)
    width = request.config.getoption("--window_width", default="1920")
    height = request.config.getoption("--window_height", default="1080")

    if use_selenoid:
        # Selenoid
        options = Options()
        options.add_argument(f"--window-size={width},{height}")
        if headless:
            options.add_argument("--headless")

        options.set_capability("browserName", browser)
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True
        })

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options
        )

    else:
        # Локальный запуск
        if browser == "chrome":
            options = Options()
            options.add_argument(f"--window-size={width},{height}")
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            driver.set_window_size(int(width), int(height))

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    yield driver

    attach.add_screenshot(driver)
    attach.add_html(driver)
    attach.add_logs(driver)

    if use_selenoid:
        attach.add_video(driver)

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid",
        action="store_true",
        default=False,
        help="Run tests in Selenoid"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox"
    )
    parser.addoption(
        "--browser_version",
        action="store",
        default="latest",
        help="Browser version"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run in headless mode"
    )
    parser.addoption(
        "--window_width",
        action="store",
        default="1920",
        help="Window width"
    )
    parser.addoption(
        "--window_height",
        action="store",
        default="1080",
        help="Window height"
    )
    parser.addoption(
        "--base_url",
        action="store",
        default="https://demo.qa.guru",
        help="Base URL for tests"
    )


@pytest.fixture
def registration_page(driver, request):
    base_url = request.config.getoption("--base_url", default="https://demo.qa.guru")
    page = RegistrationPage(driver)
    page.PAGE_URL = f"{base_url}/one-page-form/automation-practice-form.html"
    page.open()
    return page
