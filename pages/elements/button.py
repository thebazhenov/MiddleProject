from pages.components.base_components import BaseComponents

class Button(BaseComponents):

    def __init__(self, locator):
        super().__init__(locator)
        self.locator = locator

    def click(self, *args, **kwargs):
        return self.locator.click(*args, **kwargs)

    def verify_enabled(self, status: bool = True):
        if status:
            self.expect(self.locator).to_be_enabled()
        else:
            self.expect(self.locator).not_to_be_enabled()