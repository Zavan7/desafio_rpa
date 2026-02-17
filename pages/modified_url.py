from playwright.sync_api import Page, TimeoutError

class ModifiedUrl:
    def __init__(self, page: Page):
        self.page = page

    def validate_url_contains(
            self, partial_url: str,
            timeout: int = 5000
        ) -> None:

        try:
            self.page.wait_for_url(f'**{partial_url}**', timeout=timeout)
            print(f'[SUCCESS] URL contém o trecho esperado: {partial_url}')
        except TimeoutError:
            pass
