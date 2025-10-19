from page_context import PageContext, LocatorContext


class BasePage:
    def __init__(self, page: PageContext):
        self.page = page

    def locator(self, selector):
        return self.page.locator(selector)

    def wait_selector(self, selector: str, timeout: float = None) -> None:
        """
        Ожидает появления элемента на странице
        """
        self.page.wait_for_selector(selector=selector,
                                    timeout=timeout)

    def click(self, selector: str, timeout: float = None) -> None:
        """
        Кликает элемент
        """
        self.wait_selector(selector, timeout)


    @abstractmethod
    def write(self):
        pass
