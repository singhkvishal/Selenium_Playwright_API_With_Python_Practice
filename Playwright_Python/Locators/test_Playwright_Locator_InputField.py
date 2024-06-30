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
    email_Add = page.get_by_label("Email address")
    email_Add.highlight()
    #email_Add.fill('email@example.com')

    page.get_by_placeholder("Password").highlight()#.fill('Password')

    page.get_by_label("Example textarea").highlight()#.fill("Example textarea")

    browser.close()
