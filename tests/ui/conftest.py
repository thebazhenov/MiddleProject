import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def main_page(auth_page):
    return MainPage(auth_page)

@pytest.fixture
def contact_page(auth_page):
    return ContactsPage(auth_page)
