## Проект автотестов  UI + API 

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm_logo.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python_logo.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest_logo.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene_logo.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium_logo.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github_logo.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins_logo.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report_logo.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops_logo.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira_logo.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/telegram_logo.png"></code>
</p>


<!-- Тест кейсы -->

## Покрытый функционал

1. [Parabank](https://parabank.parasoft.com/parabank/) - UI
    - Регистрация пользователя
    - Авторизация пользователя
    - Поиск товара
    - Удаление товара из корзины
    - Добавление товара в корзину
2. [Reqres](https://reqres.in/) - API
   - Создание пользователя 
   - Обновление данных пользователя
   - Регистрация пользователя
   - Авторизация пользователя
   - Удаление пользователя

## Запуск тестов

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/Ui_Api_test_Parabank_Reqres/)

Для запуска тестов выбрать "Собрать сейчас"

![Jenkins](/images/screenshot/jenkins.png)

Результат о прохождении тестов присылается в телеграм, со ссылкой на Allure отчет.

![Telegram](/images/screenshot/telegram.png)

### __Примеры Allure отчётов:__ 

#### [Allure Report](https://jenkins.autotests.cloud/job/Ui_Api_test_Parabank_Reqres/3/allure/)

UI-тесты

![Allure UI](/images/screenshot/ui.png)

API-тесты

![Allure API](/images/screenshot/api.png)

Пример видео прохождения теста

![Allure vid](/images/screenshot/test.gif)

### __Интеграции с другими сервисами:__ 
[Allure TestOps](https://allure.autotests.cloud/project/3571/launches)

![Allure TestOps](/images/screenshot/allure_testops.png)

[Jira](https://jira.autotests.cloud/browse/HOMEWORK-823)

![Allure TestOps](/images/screenshot/jira.png)
