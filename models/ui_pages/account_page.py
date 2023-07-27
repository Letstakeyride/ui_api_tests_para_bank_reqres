import time
from faker import Faker
from selene import browser, have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from models.ui_pages.base_page import BasePage
from allure import step
from selene import query

fake = Faker()


class AccountPage(BasePage):

    def __init__(self):
        self.from_account_id = None
        self.new_account_balance = None
        self.new_account_id = None

        self.amount = fake.random_int(min=1, max=100)

    @staticmethod
    def open_new_account_page():
        with step('Открыть страницу создания нового счёта'):
            time.sleep(3)
            browser.open('/openaccount.htm')
            time.sleep(3)

    @staticmethod
    def open_transfer_funds_page():
        with step('Открыть страницу перевода средств'):
            time.sleep(3)
            browser.open('/transfer.htm')
            time.sleep(3)

    def open_new_account(self, type_account):
        with step(f'Создание нового аккаунта типа {type_account}'):
            s('#type').send_keys(type_account).press_enter()
            s('#rightPanel > div > div > form > div > input').should(be.visible).double_click()
            s('#rightPanel > div > div > p:nth-child(2)').should(
                have.exact_text('Congratulations, your account is now open.'))
            self.new_account_id = s('#newAccountId').get(query.text)

    def check_opened_account(self):
        with step('Проверка созданного аккаунта'):
            s('#newAccountId').should(be.visible).click()
            (s('#accountId').should(be.visible)).should(have.exact_text(self.new_account_id))

    def transfer_funds(self):
        with step('Перевод средств на новый аккаут '):
            self.fill_input('#amount', self.amount)
            self.from_account_id = s('#fromAccountId > option:nth-child(1)').get(query.text)
            s('#toAccountId').click().send_keys(self.new_account_id).press_enter()
            s('[value="Transfer"]').click()
            s('#rightPanel > div > div > h1').should(have.exact_text('Transfer Complete!'))

    def check_transfer_funds(self):
        with step('Проверка перевода средств'):
            s('#rightPanel > div > div > p:nth-child(2)').should(
                have.exact_text(
                    f'${"{:.2f}".format(self.amount)} has been transferred from account #{self.from_account_id} to account '
                    f'#{self.new_account_id}.'))

    @staticmethod
    def prepare_site_for_tests():
        with step('Подготовка сайта к автоматизации'):
            browser.open('/admin.htm')
            s('button.button[name="action"][value="INIT"]').double_click()
            s('button.button[name="action"][value="CLEAN"]').double_click()
            s('#accessMode3').double_click()
            s('input[type="submit"][value=Submit].button').double_click()
