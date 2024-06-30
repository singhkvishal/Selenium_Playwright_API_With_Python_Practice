from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()
    page = brcx.new_page()

    #--CSS Selector--
    # 1- Tagename
    # 2- Classname
    # 3- Id
    # 4- Attribute/Vale

    page.goto("https://bootswatch.com/default")

    # 1- Tagename
    page.locator("css=h1").highlight()

    # 2-Classname
    page.locator("css=button.btn-outline-success").highlight()

    # 3-Id
    page.locator("css=button#btnGroupDrop1").highlight()

    # 4-Attribute/Vale
    page.locator("css=input[readonly]").highlight()
    page.locator("css=input[value='correct value']").highlight()
    browser.close()
