from playwright.sync_api import Playwright, sync_playwright, Page
from automacao_mandeumzap.utils.elements_identifiers import (
    LOGIN_BUTTON,
    LOGIN_PASSWORD,
    LOGIN_USERNAME,
    NOW,
    TICKET_REPORT,
    EXIBIR_FILTROS_BUTTON,
    NOME_FILTER
)

import time
from dotenv import load_dotenv, dotenv_values

load_dotenv()

env = dotenv_values()

def login(page: Page):
    page.locator(LOGIN_USERNAME).type(env['USERNAME'])
    page.locator(LOGIN_PASSWORD).type(env['PASSWORD'])
    page.locator(LOGIN_BUTTON).click()

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, channel='chrome')
    page = browser.new_page()
    page.goto('https://agilizzapromotora.mandeumzap.com.br/login')
    
    login(page)

    while (True):        
        time.sleep(1)
        page.evaluate('(NOW) => document.querySelector(NOW).click()', NOW)

        page.locator(EXIBIR_FILTROS_BUTTON).click()
        page.locator(NOME_FILTER).type('ATENDIMENTO')

        time.sleep(1)
        page.mouse.wheel(300, 300)

        time.sleep(10)
        page.evaluate('(TICKET_REPORT) => document.querySelector(TICKET_REPORT).click()', TICKET_REPORT)        

        time.sleep(1)
        page.mouse.wheel(300, 300)

        time.sleep(9)

def main():
    with sync_playwright() as Playwright:
        run(Playwright)
main()