import asyncio
from playwright.async_api import async_playwright, Playwright, Page
from automacao_mandeumzap.utils.elements_identifiers import (
    LOGIN_BUTTON,
    LOGIN_PASSWORD,
    LOGIN_USERNAME,
    NOW,
    TICKET_REPORT
)
import time
from dotenv import load_dotenv, dotenv_values

load_dotenv()

env = dotenv_values()

async def login(page: Page):
    await page.locator(LOGIN_USERNAME).type(env['USERNAME'])
    await page.locator(LOGIN_PASSWORD).type(env['PASSWORD'])
    await page.locator(LOGIN_BUTTON).click()

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, channel='chrome')
    page = await browser.new_page()
    await page.goto('https://agilizzapromotora.mandeumzap.com.br/login')
    
    await login(page)

    while (True):
        nowButton = page.locator(NOW)
        
        time.sleep(1)
        await page.evaluate('(NOW) => document.querySelector(NOW).click()', NOW)

        time.sleep(10)
        ticket_report_button = page.locator(TICKET_REPORT)
        await page.evaluate('(TICKET_REPORT) => document.querySelector(TICKET_REPORT).click()', TICKET_REPORT)        

        time.sleep(10)

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())