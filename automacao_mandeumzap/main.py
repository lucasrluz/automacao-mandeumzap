from playwright.sync_api import Playwright, sync_playwright, Page
from utils.elements_identifiers import (
    LOGIN_BUTTON,
    LOGIN_PASSWORD,
    LOGIN_USERNAME,
    NOW,
    TICKET_REPORT,
    EXIBIR_FILTROS_BUTTON,
    NOME_FILTER,
    EXIBIR_FILTROS_ESTATISTICAS_BUTTON,
    INIT_DATE_FILTER,
    END_DATE_FILTER,
    APLICAR_FILTRO_BUTTON
)

import time
from dotenv import load_dotenv, dotenv_values

load_dotenv()

env = dotenv_values('.env')

def login(page: Page):
    page.locator(LOGIN_USERNAME).type(env['USERNAME'])
    page.locator(LOGIN_PASSWORD).type(env['PASSWORD'])
    page.locator(LOGIN_BUTTON).click()

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
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

        page.evaluate('(EXIBIR_FILTROS_ESTATISTICAS_BUTTON) => document.querySelector(EXIBIR_FILTROS_ESTATISTICAS_BUTTON).click()', EXIBIR_FILTROS_ESTATISTICAS_BUTTON)

        init_date = page.evaluate('(INIT_DATE_FILTER) => document.querySelector(INIT_DATE_FILTER).value', INIT_DATE_FILTER)

        end_date = page.evaluate('(END_DATE_FILTER) => document.querySelector(END_DATE_FILTER).value', END_DATE_FILTER)

        init_date_formated = end_date[0:5] + init_date[5:16]

        time.sleep(2)
        page.type(INIT_DATE_FILTER, init_date_formated)
        page.click(APLICAR_FILTRO_BUTTON)

        time.sleep(1)
        page.mouse.wheel(500, 500)

        time.sleep(9)

def main():
    with sync_playwright() as Playwright:
        run(Playwright)
main()
