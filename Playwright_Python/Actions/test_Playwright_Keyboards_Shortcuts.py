from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    brcx = browser.new_context()

    # Create a new page
    page = brcx.new_page()
    # Visit the playwright website
    page.goto("https://bootswatch.com/default/")
    textArea=page.locator("//textarea[@id='exampleTextarea']")
    textArea.clear()

    textArea.press("KeyW")
    textArea.press("KeyO")
    textArea.press("KeyR")

    textArea.press("Shift+KeyD")
    textArea.press("Control+ArrowLeft")
