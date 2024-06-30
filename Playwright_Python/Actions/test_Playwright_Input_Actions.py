from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    page = brcx.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    try:
        input= page.locator("//*[@name='email']")
        input.highlight()
        #input.fill("sdas@gmail.com")
        input.type("sdas@gmail.com")

    except:
        print("error")

    browser.close()
