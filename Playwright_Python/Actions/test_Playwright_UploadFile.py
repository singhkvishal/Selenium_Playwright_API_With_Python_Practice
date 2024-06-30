from playwright.sync_api import  sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=500)
    brcox=browser.new_context()

    page=brcox.new_page()
    page.goto("https://bootswatch.com/default/")
    uploadFile=page.locator("//*[@id='formFile']")
    uploadFile.set_input_files("file.text")
    uploadFile.set_input_files(["file.text","File1.text"]) # Upload Multipal Files

    with page.expect_file_chooser() as fc_info:
        page.locator("//*[@id='formFile']").click()
        file_chooser = fc_info.value
        file_chooser.set_files("myfile.pdf")
    page.close()