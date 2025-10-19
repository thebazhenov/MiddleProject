

class TestLoginPage:

    def test_login_page(self, login_page, user_credentials):
        login_page.goto()
        login_page.login(user_credentials.username, user_credentials.password)

