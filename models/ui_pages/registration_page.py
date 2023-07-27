from selene import have
from selene.support.shared.jquery_style import s
from models.ui_pages.base_page import BasePage
from allure import step


class RegistrationPage(BasePage):

    def input_full_name(self, first_name, last_name):
        with step(f'Ввод имени {first_name} и фамилии {last_name}'):
            self.fill_input('#customer\.firstName', first_name)
            self.fill_input('#customer\.lastName', last_name)

    def input_residential_address(self, address, city, state, zip_code):
        with step('Ввод адреса'):
            self.fill_input('#customer\.address\.street', address)
            self.fill_input('#customer\.address\.city', city)
            self.fill_input('#customer\.address\.state', state)
            self.fill_input('#customer\.address\.zipCode', zip_code)

    def input_contact_data(self, phone, ssn):
        with step('Ввод контактных данных'):
            self.fill_input('#customer\.phoneNumber', phone)
            self.fill_input('#customer\.ssn', ssn)

    def input_login_and_password(self, login, password):
        with step(f'Ввод логина  {login} и пароля'):
            self.fill_input('#customer\.username', login)
            self.fill_input('#customer\.password', password)
            self.fill_input('#repeatedPassword', password)

    @staticmethod
    def click_register_button():
        with step('Регистрация'):
            s('[value="Register"]').click()

    @staticmethod
    def check_register(login):
        with step('Проверка регистрации'):
            s('#rightPanel > h1').should(have.exact_text(f'Welcome {login}'))
