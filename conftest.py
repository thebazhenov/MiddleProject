import os
from typing import Any, Generator
import pytest
from dotenv import load_dotenv
from dataclasses import dataclass

from pages.mail_pages.inbox_page import InboxPage

load_dotenv()

from pages.login_page import LoginPage


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
def storage_state_path():
    return "storage_state.json"


@pytest.fixture(scope="session")
def force_refresh_auth():
    """Флаг для принудительного обновления аутентификации"""
    return os.getenv("FORCE_REFRESH_AUTH", "false").lower() == "true"


@pytest.fixture(scope="session")
def ensure_storage_state(storage_state_path, browser, base_url, user_credentials, force_refresh_auth):
    # Удаляем файл если он существует и установлен флаг принудительного обновления
    if force_refresh_auth and os.path.exists(storage_state_path):
        os.remove(storage_state_path)

    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    login_page = LoginPage(page)
    main_page = InboxPage(page)
    login_page.open()
    login_page.login(user_credentials.username, user_credentials.password)

    # Проверка входа
    try:
        main_page.verify_url()
    except Exception as e:
        pytest.raises(Exception)

    context.storage_state(path=storage_state_path)
    context.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, storage_state_path, ensure_storage_state):
    return {
        **browser_context_args,
        "storage_state": storage_state_path,
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