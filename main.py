'''
Docstring for main

Practice_test_automation
'''
from pages.practice_page import InitialPage
from playwright.sync_api import sync_playwright
 
url = 'https://practicetestautomation.com/'
seletor_um = '#menu-item-20'


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    testando = InitialPage(url, seletor_um)
    testando.practrice_page(page)

    browser.close()
