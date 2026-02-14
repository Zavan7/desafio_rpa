from playwright.sync_api import Page

class InitialPage:
    def __init__ (self, url: str, seletor_page: str, timeout=4000):
        self.url = url
        self.seletor_page = seletor_page
        self.timeout = timeout

    def practrice_page(self, page: Page) -> True:
        '''
        Docstring for pactrice_page
        
        :param self: Description
        :param page: Description
        :type page: Page

        Tenta acessar a URL, e localizar o seletor, para iniciar o desafio
        '''

        
        try:
            page.goto(self.url)

            page.wait_for_selector (
                self.seletor_page,
                timeout = self.timeout
            )
            button = page.locator(self.seletor_page)

            if not button.is_visible() and button.is_enabled():
                return None
            
            button.click()
            print('Log de sucesso aqui')
            return True
        
        except Exception as e:
            print(f'Log de erro aqui: {e}')
            return False
            