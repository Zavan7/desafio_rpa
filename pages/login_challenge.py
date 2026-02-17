'''
Docstring for pages.login_challenge
'''

from playwright.sync_api import Page

class LoginChallenge:
    def __init__(
            self, page: Page,
            user_selector: str,
            password_selector: str,
            button_selector: str,
            locator_challenge_one: str,
            timeout=4000,
        ):

        self.page = page
        self.user_selector = user_selector
        self.password_selector = password_selector
        self.button_selector = button_selector
        self.locator_challenge_one = locator_challenge_one
        self.timeout = timeout

    def challenge_page(self):
        try:
            self.page.wait_for_selector(
                self.locator_challenge_one,
                timeout= self.timeout
            )
            self.page.get_by_role("link", name="Test Login Page").click()
            
            print('Log de SUCESSO aqui (Test login page)')

        except Exception as e:
            print(f'Log de erro aqui {e}')

    def first_login_challeng(self, login_user: str, password: str):
        try:
            self.page.wait_for_selector(
                self.user_selector,
                timeout=self.timeout
            )

            self.page.locator(self.user_selector).fill(login_user)
            self.page.locator(self.password_selector).fill(password)
        
            self.page.locator(self.button_selector).click()
            print('Log de SUCESSO aqui (SUCESSO ao realizar login)')

        except Exception as e:
            print(f'Log de erro aqui {e}')