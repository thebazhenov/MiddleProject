
import os
from typing import Any, Generator

import pytest
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

from pages.login_page import LoginPage
# from page_objects.site import SiteListPage

@dataclass
class Credentials:
    username: str
    password: str


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("PYTEST_BASE_URL")

@pytest.fixture(scope="session")
def user_credentials() -> Credentials:
    return Credentials(
        username=os.getenv("ADMIN_USERNAME"),
        password=os.getenv("ADMIN_PASSWORD"),
    )


@pytest.fixture(scope="session")
def ensure_storage_state(storage_state_path, browser, base_url, user_credentials):
    if not os.path.exists(storage_state_path):
        context = browser.new_context(base_url=base_url)
        page = context.new_page()
        login_page = LoginPage(page)
        # site_list_page = SiteListPage(page)
        login_page.goto()
        login_page.login(user_credentials.username, user_credentials.password)
        # site_list_page.verify_url()
        context.storage_state(path=storage_state_path)
        context.close()


@pytest.fixture(scope="session")
def storage_state_path():
    return "storage_state.json"


@pytest.fixture(scope="session")
def browser_context_args(storage_state_path, ensure_storage_state, base_url):
    return {
        "base_url": base_url,
    }


@pytest.fixture
def auth_page(browser, storage_state_path, ensure_storage_state, base_url) -> Generator[Any, Any, None]:
    context = browser.new_context(
        storage_state=storage_state_path,
        base_url=base_url,
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
