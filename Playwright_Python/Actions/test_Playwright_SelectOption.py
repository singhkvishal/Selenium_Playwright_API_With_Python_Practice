from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    page = brcx.new_page()
    page.goto("https://bootswatch.com/default/")

    #Check Box
    try:
        SelectList= page.locator("//select[@id='exampleSelect1']").nth(0)
        SelectList.select_option("4")
    except:
        print("error")

    selectMulti=page.locator("xpath=//select[@id='exampleSelect2']")
    selectMulti.select_option(["2","3","4"])
    page.close()
