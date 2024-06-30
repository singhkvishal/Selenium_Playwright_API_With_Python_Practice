from playwright.async_api import BrowserContext
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    # Create a new page
    page = brcx.new_page()
    # Visit the playwright website
    page.goto("https://playwright.dev/")
    try:
        button=page.locator("//a[@class='getStarted_Sjon']")
        button.click()
        page.locator("//a[text()='Introduction']").dblclick()
        page.locator("//a[text()='Introduction']").dblclick(delay=500)
        page.locator("//a[text()='Introduction']").click(button="right")
        page.locator("//a[text()='Introduction']").click(modifiers=["Shift"])
        page.locator("//a[text()='Introduction']").click(modifiers=["Shift","Meta"])

        page.locator("//a[text()='Python'][@class='navbar__link']").hover()
    except:
        print("error")

    browser.close()
