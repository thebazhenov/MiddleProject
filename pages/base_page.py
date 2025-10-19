from playwright.sync_api import expect, Page
from pages.page_components import PageComponents

class BasePage:
    def __init__(self, page: Page, path: str, query_params: dict | None = None):
        self.page = page
        self.path = path
        self.query_params = query_params
        self.expect = expect

    @property
    def page_components(self) -> PageComponents:
        return PageComponents(self.page)

    def expect(self, *args, **kwargs):
        return self.expect(*args, **kwargs)

    def locator(self, selector):
        return self.page.locator(selector)

    def wait_selector(self, selector: str, timeout: float = None) -> None:
        """
        Ожидает появления элемента на странице
        """
        self.page.wait_for_selector(selector=selector,
                                    timeout=timeout)

    def _build_url(self) -> str:
        if not self.query_params:
            return self.path
        search_params = "&".join(
            f"{k}={v}" for k, v in self.query_params.items()
        )
        return f"{self.path}?{search_params}"

    def goto(self) -> None:
        self.page.goto(self._build_url())

    def verify_url(self, query_params: dict | None = None) -> None:
        if query_params:
            self.query_params = query_params
        expect(self.page).to_have_url(self._build_url())
