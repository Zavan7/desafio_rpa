'''
Docstring for main

Practice_test_automation
'''
from playwright.sync_api import sync_playwright
from time import sleep

from pages.practice_page import InitialPage


url = 'https://practicetestautomation.com/'
seletor_um = '#menu-item-20'


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    testando = InitialPage(url, seletor_um)
    testando.practrice_page(page)
    sleep(10)

    browser.close()
