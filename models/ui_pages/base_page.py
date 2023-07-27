from selene import browser
from allure import step
from selene.support.shared.jquery_style import s


class BasePage:

    @staticmethod
    def open_registration_page():
        with step('Открыть страницу регистрации'):
            browser.open('/register.htm')

    @staticmethod
    def open_login_page():
        with step('Открыть страницу авторизации'):
            browser.open('/index.htm')

    @staticmethod
    def open_customer_lookup_page():
        with step('Открыть страницу поиска аккаунта'):
            browser.open('/lookup.htm')

    @staticmethod
    def logout():
        with step('Разлогиниться'):
            s('#leftPanel > ul > li:nth-child(8) > a').click()

    @staticmethod
    def fill_input(locator, text):
        s(locator).send_keys(text)
