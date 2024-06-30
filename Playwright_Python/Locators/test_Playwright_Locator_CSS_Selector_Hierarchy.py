from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()
    page = brcx.new_page()

    page.goto("https://bootswatch.com/default")


    page.locator("css=nav.bg-dark a.nav-link.active").highlight()
    page.locator("css=div.bs-component > ul.list-group").highlight()

    browser.close()
