import allure
from faker import Faker
import json
import os.path
from requests import Session
from curlify import to_curl
import logging
from datetime import datetime

from utils import attach


def generate_first_name():
    fake = Faker()
    return fake.first_name()


def generate_last_name():
    fake = Faker()
    return fake.last_name()


def generate_address():
    fake = Faker()
    return fake.address()


def generate_city():
    fake = Faker()
    return fake.city()


def generate_state():
    fake = Faker()
    return fake.state()


def generate_zip_code():
    fake = Faker()
    return fake.zipcode()


def generate_phone():
    fake = Faker()
    return fake.phone_number()


def generate_ssn():
    fake = Faker()
    return fake.ssn()


def load_json_schema(file_name: str):
    path_schema = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../schemas', file_name)
    with open(path_schema) as schema_json:
        return json.loads(schema_json.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs):
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)

        msg = to_curl(response.request)
        status_code = response.status_code
        logging.info(f'{datetime.now()}\nstatus_code={status_code}\n{msg}')
        with allure.step(f'{method} {url}'):
            attach.add_request(status_code, msg)

            try:
                response_body = response.json()
            except json.JSONDecodeError:
                response_body = response.text

            attach.add_response(response_body)

        return response
