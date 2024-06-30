from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()
    page = brcx.new_page()

    page.goto("https://bootswatch.com/default")
    page.get_by_title("attribute").highlight()
    page.get_by_title("Source Title").highlight()

    browser.close()
