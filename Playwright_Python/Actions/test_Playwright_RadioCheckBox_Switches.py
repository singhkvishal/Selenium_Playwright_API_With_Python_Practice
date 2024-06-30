from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    page = brcx.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")

    #Check Box
    try:
       Checkbox= page.locator("//*[@name='chkSelectAll']").nth(0)
       if  Checkbox.is_checked()==False:
        Checkbox.check()

        if  Checkbox.is_checked():
             Checkbox.uncheck()

        Checkbox.set_checked(True)
    except:
        print("error")

    #Radio Button
    page.goto("https://bootswatch.com/default/")
    page.locator("//input[@id='optionsRadios2']").check()

    #Switches
    page.locator("//input[@id='flexSwitchCheckChecked']").check()
    page.locator("//input[@id='flexSwitchCheckChecked']").uncheck()
    browser.close()
