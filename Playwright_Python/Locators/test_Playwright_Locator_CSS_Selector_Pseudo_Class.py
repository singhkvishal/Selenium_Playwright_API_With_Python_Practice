from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()
    page = brcx.new_page()

    page.goto("https://bootswatch.com/default")


    page.locator("css=h1:text('Navbars')").highlight()
    page.locator("css=h1:text('Nav')").highlight()
    page.locator("css=h1:text-is('Navs')").highlight()

    #page.locator("css=div:dropdown-menu:visible").highlight()

    # nth selector

    page.locator("button.btn-primary").nth(4).highlight()

    page.locator("button.btn-primary").locator("nth=4").highlight()

    #move to parent locator
    page.locator("Email address").locator("..").highlight()

    #using Filter
    page.get_by_role("Heading").filter(has_text="Heading").highlight()
    page.locator("div.form-group").filter(has=page.get_by_label("Password")).highlight()
    browser.close()
