'''
Docstring for main

Practice_test_automation
'''
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from time import sleep
import time
import os

from pages.practice_page import InitialPage
from pages.login_challenge import LoginChallenge
from pages.modified_url import ModifiedUrl
from pages.final_validations import FinalValidations

# =========================
# Environment Configuration
# =========================
# Load environment variables for secure credential handling
load_dotenv()

LOGIN_USER = os.getenv('USERNAME')
PASSWORD_USER = os.getenv('PASSWORD')


def first_challenge():

    result = {
        'start_date': None,
        'end_date': None,
        'duration': None,
        'status': None,
        'message': None,
        'error': None
    }

    start_date = time.time()
    status = None
    message = None
    error = None

    try:
        # =========================
        # Test Data & Selectors Setup
        # =========================
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

            desired_url = 'practicetestautomation.com/logged-in-successfully/'

            modified = ModifiedUrl(page)
            modified.validate_url_contains(desired_url)

            log_out_button_select = '.wp-block-button'
            selector_msg_success = '.has-text-align-center'
            msg_success = "Congratulations student. You successfully logged in!"

            validacao_final = FinalValidations(page)

            validacao_final.validate_success_message(
                selector_msg_success,
                msg_success
            )

            validacao_final.validate_logout_button(
                log_out_button_select
            )

            browser.close()

            status = 'success'
            message = 'Login realizado e validado com sucesso.'

    except Exception as e:
        status = 'fail'
        message = 'Erro durante execução da automação.'
        error = str(e)

    finally:
        end_date = time.time()
        duration = end_date - start_date

        result['start_date'] = time.strftime(
            '%d/%m/%Y %H:%M:%S',
            time.localtime(start_date)
        )

        result['end_date'] = time.strftime(
            '%d/%m/%Y %H:%M:%S',
            time.localtime(end_date)
        )

        result['duration'] = f'{duration:.2f}'
        result['status'] = status
        result['message'] = message
        result['error'] = error

        for i, j in result.items():
            print(i, j)

    return result
if __name__ == '__main__':
    first_challenge()
    