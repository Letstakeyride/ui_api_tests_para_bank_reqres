from allure import step
from selene import browser, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from models.ui_pages.base_page import BasePage


class AuthorizationPage(BasePage):

    def input_login_and_password(self, login, password):
        with step(f'Ввод логина {login} и пароля'):
            self.fill_input('[name="username"]', login)
            self.fill_input('[name="password"]', password)

    @staticmethod
    def click_login_button():
        s('[value="Log In"]').click()

    @staticmethod
    def check_success_login(first_name, last_name):
        with step('Проверка авторизации'):
            s('#leftPanel > p').should(have.exact_text(f'Welcome {first_name} {last_name}'))

    def login(self, login, password):
        with step(f'Авторизация под {login}'):
            browser.open('/index.htm')
            self.fill_input('[name="username"]', login)
            self.fill_input('[name="password"]', password)
            s('[value="Log In"]').click()
