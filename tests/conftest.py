import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from utils import attach
from utils.helper import CustomSession


@pytest.fixture(scope='session')
def reqres():
    return CustomSession(base_url=os.getenv("base_url_regres"))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def web_browser():
    options = Options()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '100.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)

    s_login = os.getenv('LOGIN')
    s_password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{s_login}:{s_password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser.config.driver = driver
    browser.config.base_url = os.getenv('base_url')

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
