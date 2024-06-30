from playwright.async_api import BrowserContext
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    # Create a new page
    page = brcx.new_page()
    # Visit the playwright website
    page.goto("https://unsplash.com/")

    email_Add = page.get_by_alt_text("a kitchen with three stools next to a counter")
    email_Add.highlight()

    page.get_by_alt_text("A woman in a white shirt and black pants").click()

    browser.close()
