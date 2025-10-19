from pages.components.layout_menu_components import LayoutMenuComponents
from context.page_context import PageContext
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page: PageContext, path: str, query_params: dict | None = None):
        self.page = page
        self.path = path
        self.query_params = query_params
        self._expect = expect(self.page)

    @property
    def layout_menu(self) -> LayoutMenuComponents:
        return LayoutMenuComponents(self.page)

    @property
    def expect(self):
        """Доступ к expect через свойство"""
        return self._expect

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

    def open(self) -> None:
        url = self._build_url()
        self.page.goto(url)
        expect(self.page).to_have_url(url)

    def verify_url(self, query_params: dict | None = None, timeout: float = 5000) -> None:
        if query_params:
            self.query_params = query_params
        self._expect.to_have_url(self._build_url(), timeout=timeout)

    def verify_url_not_changed(self, original_url: str = None) -> None:
        """Проверяет, что URL не изменился"""
        if original_url is None:
            # Если URL не передан, используем текущий построенный URL
            original_url = self._build_url()
        self._expect.to_have_url(original_url)
