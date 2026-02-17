'''
Docstring for main

Practice_test_automation
'''
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from time import sleep
import os

from pages.practice_page import InitialPage
from pages.login_challenge import LoginChallenge
from pages.modified_url import ModifiedUrl

load_dotenv()

LOGIN_USER = os.getenv('USERNAME')
PASSWORD_USER = os.getenv('PASSWORD')

def first_challenge():
    url = 'https://practicetestautomation.com/'
    selector_challenge_one = '#menu-item-20'
    test_login_page = 'a[href*="practice-test-login"]'
    locator_login = '#username'
    locator_password = '#password'
    submit_button = '#submit'

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        initial_page = InitialPage(url, selector_challenge_one)
        initial_page.practrice_page(page)

        login_page = LoginChallenge(
            page,
            locator_login,
            locator_password,
            submit_button,
            test_login_page
        )
        login_page.challenge_page()
        login_page.first_login_challeng(LOGIN_USER, PASSWORD_USER)

        sleep(5)

        browser.close()


def challenge_validation():
    ...

if __name__ == '__main__':
    first_challenge()