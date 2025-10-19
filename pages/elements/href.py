from pages.components.base_components import BaseComponents

class Href(BaseComponents):

    def __init__(self, locator):
        super().__init__(locator)
        self.locator = locator

    def click(self, *args, **kwargs):
        return self.locator.click(*args, **kwargs)