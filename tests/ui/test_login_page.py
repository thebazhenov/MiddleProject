import allure
import pytest
from pages.mail_pages.inbox_page import InboxPage


@pytest.fixture
def inbox_page_no_auth(page):
    return InboxPage(page)


class TestLoginPage:

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_page(self, login_page, inbox_page_no_auth, user_credentials):
        login_page.open()
        login_page.login(user_credentials.username, user_credentials.password)
        inbox_page_no_auth.verify_url()

    @pytest.mark.parametrize(
        "login, password, allure_title",
        [
            ("t", "", "Вход в систему с пустым паролем"),
            ("", "password", "Вход в систему с пустым логином"),
            ("", "", "Вход в систему с пустыми данными")
        ]
    )
    def test_login_page_negative(self, login_page, login, password, allure_title):
        allure.dynamic.title(allure_title)
        login_page.open()
        login_page.login(login, password)
        login_page.verify_url_not_changed()
