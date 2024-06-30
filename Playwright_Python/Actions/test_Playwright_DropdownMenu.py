from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=100)
    brcx=browser.new_context()

    page=brcx.new_page()
    page.goto("https://bootswatch.com/default/")

    themes=page.locator("xpath=//a[@id='themes']")
    themes.click()
    page.locator("xpath=//div[@class='dropdown-menu show']//a[@href='../united/']").click()

    page.close()
