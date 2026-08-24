import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from pages.registration_page import RegistrationPage
from utils import attach

load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASSWORD")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope="function")
def driver(request):
    use_selenoid = request.config.getoption("--selenoid", default=False)

    if use_selenoid:
        options = Options()
        options.add_argument("--window-size=1920,1080")

        options.set_capability("browserName", "chrome")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True
        })

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options
        )
    else:
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

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


@pytest.fixture
def registration_page(driver):
    page = RegistrationPage(driver)
    page.open()
    return page
