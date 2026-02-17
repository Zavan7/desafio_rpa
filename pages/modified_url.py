'''
Docstring for pages.modified_url
'''
from playwright.sync_api import Page

class ModifiedUrl:
    def __init__(self, desired_url: str, current_url):
        self.desired_url = desired_url
        self.current_url = current_url

    def validate_url(self):
        try:
            if self.desired_url == self.current_url:
                print ('Log de sucesso aqui, url correta')
                return f'URL está correta {self.desired_url}'
            return None
        
        except Exception as e:
            print(f'Log de erro na url {e}')