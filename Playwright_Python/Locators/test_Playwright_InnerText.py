from playwright.async_api import BrowserContext
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    # Create a new page
    page = brcx.new_page()
    # Visit the playwright website
    page.goto("https://bootswatch.com/default/")

    # Locate a link element with "Docs" text
    email_Add = page.get_by_text("Heading 5")
    email_Add.highlight()

    page.get_by_text("Small button").highlight()

    page.get_by_text("Right").highlight()
    page.get_by_text("fine print").highlight()

    page.get_by_text("fine print",exact=True).highlight()
    browser.close()
