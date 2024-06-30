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
    def_button = page.get_by_role('button', name="Default button")
    def_button.click()

    heading=page.get_by_role("heading",name="Heading 2")
    heading.highlight()

    radiobtn=page.get_by_role('radio', name="Option one is this and that—be sure to include why it's great")
    radiobtn.highlight()
    radiobtn.check()

    chekBox=page.get_by_role('checkbox', name="Default checkbox")
    chekBox.highlight()
    chekBox.check()

    # Get the url
    print("Docs:", page.url)
    browser.close()
