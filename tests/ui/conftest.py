import pytest
from pages.login_page import LoginPage
from pages.mail_pages.inbox_page import InboxPage
from pages.mail_pages.drafts_page import DraftsPage
from pages.mail_pages.sent_page import SentPage
from pages.contacts_page import ContactsPage
from pages.settings_page import SettingPage



@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inbox_page(auth_page):
    return InboxPage(auth_page)

@pytest.fixture
def drafts_page(auth_page):
    return DraftsPage(auth_page)

@pytest.fixture
def sent_page(auth_page):
    return SentPage(auth_page)

@pytest.fixture
def contact_page(auth_page):
    return ContactsPage(auth_page)

@pytest.fixture
def setting_page(auth_page):
    return SettingPage(auth_page)