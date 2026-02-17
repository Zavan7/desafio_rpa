'''
Docstring for pages.final_validations
'''

from playwright.sync_api import Page, expect


class FinalValidations:
    def __init__(self, page: Page):
        self.page = page

    def validate_success_message(
        self,
        selector_msg: str,
        msg_success: str,
    ) -> None:
        """
        Validate if the success message matches the expected text.
        """

        try:
            expect(self.page.locator(selector_msg)).to_have_text(msg_success)
            print("Validação da mensagem OK")

        except Exception as e:
            print(f"Erro na validação da mensagem: {e}")
            raise

    def validate_logout_button(
        self,
        logout_button: str,
    ) -> None:
        """
        Validate if the logout button is visible.
        """

        try:
            expect(self.page.locator(logout_button)).to_be_visible()
            print("Validação do botão logout OK")

        except Exception as e:
            print(f"Erro na validação do botão logout: {e}")
            raise
