from selene import have
from selene.support.shared.jquery_style import s
from models.ui_pages.base_page import BasePage
from allure import step


class LookupPage(BasePage):

    def input_full_name(self, first_name, last_name):
        with step(f'Ввод имени {first_name} и фамилии {last_name}'):
            self.fill_input('#firstName', first_name)
            self.fill_input('#lastName', last_name)

    def input_residential_address(self, address, city, state, zip_code):
        with step('Ввод адреса'):
            self.fill_input('#address\.street', address)
            self.fill_input('#address\.city', city)
            self.fill_input('#address\.state', state)
            self.fill_input('#address\.zipCode', zip_code)

    def input_contact_data(self, ssn):
        with step('Ввод контактных данных'):
            self.fill_input('#ssn', ssn)

    @staticmethod
    def click_find_login_button():
        with step('Поиск аккаунта'):
            s('[value="Find My Login Info"]').click()

    @staticmethod
    def check_found_account(first_name, last_name):
        with step('Проверка найденного аккаунта'):
            s('#leftPanel > p').should(have.exact_text(f'Welcome {first_name} {last_name}'))
