import os
import pytest
from models.ui_pages.authorization_page import AuthorizationPage
from models.ui_pages.base_page import BasePage
from models.ui_pages.account_page import AccountPage
from models.ui_pages.lookup_page import LookupPage
from models.ui_pages.registration_page import RegistrationPage

from utils.helper import *
import allure

base_page = BasePage()
reg_page = RegistrationPage()
lookup_page = LookupPage()
account_page = AccountPage()
auth_page = AuthorizationPage()


class TestParaBankUI:
    ACCOUNT_DATA = [
        (generate_first_name(), generate_last_name(), generate_address(), generate_city(), generate_state(),
         generate_zip_code(), generate_phone(), generate_ssn())
    ]

    @allure.tag('UI')
    @allure.title('Подготовка сайта к тестам, сброс бд')
    def test_prepare(self, web_browser):
        account_page.prepare_site_for_tests()

    @allure.tag('UI')
    @allure.title('Регистрация пользователя')
    @pytest.mark.parametrize('first_name, last_name, address, city, state, zip_code, phone, ssn', ACCOUNT_DATA)
    def test_registration(self, web_browser, first_name, last_name, address, city, state, zip_code, phone, ssn,
                          ):
        reg_page.open_registration_page()
        reg_page.input_full_name(first_name, last_name)
        reg_page.input_residential_address(address, city, state, zip_code)
        reg_page.input_contact_data(phone, ssn)
        reg_page.input_login_and_password(os.getenv('user_login'), os.getenv('user_password'))
        reg_page.click_register_button()
        reg_page.check_register(os.getenv('user_login'))
        reg_page.logout()

    @allure.tag('UI')
    @allure.title('Поиск аккаунта')
    @pytest.mark.parametrize('first_name, last_name, address, city, state, zip_code, phone, ssn', ACCOUNT_DATA)
    def test_lookup(self, web_browser, first_name, last_name, address, city, state, zip_code, phone, ssn):
        lookup_page.open_customer_lookup_page()
        lookup_page.input_full_name(first_name, last_name)
        lookup_page.input_residential_address(address, city, state, zip_code)
        lookup_page.input_contact_data(ssn)
        lookup_page.click_find_login_button()
        lookup_page.check_found_account(first_name, last_name)
        lookup_page.logout()

    @allure.tag('UI')
    @allure.title('Авторизация')
    @pytest.mark.parametrize('first_name, last_name, address, city, state, zip_code, phone, ssn', ACCOUNT_DATA)
    def test_auth(self, web_browser, first_name, last_name, address, city, state, zip_code, phone, ssn):
        auth_page.open_login_page()
        auth_page.input_login_and_password(os.getenv('user_login'), os.getenv('user_password'))
        auth_page.click_login_button()
        auth_page.check_success_login(first_name, last_name)

    @allure.tag('UI')
    @allure.title('Создание нового счёта')
    @pytest.mark.parametrize('type_account', ['CHECKING', 'SAVINGS'])
    def test_open_new_account(self, web_browser, type_account):
        auth_page.login(os.getenv('user_login'), os.getenv('user_password'))
        account_page.open_new_account_page()
        account_page.open_new_account(type_account)
        account_page.check_opened_account()

    @allure.tag('UI')
    @allure.title('Перевод средств на новый счёт')
    def test_transfer_funds(self, web_browser):
        auth_page.login(os.getenv('user_login'), os.getenv('user_password'))
        account_page.open_transfer_funds_page()
        account_page.transfer_funds()
        account_page.check_transfer_funds()
