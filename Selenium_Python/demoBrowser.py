from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
#service_obj = Service("/Users/baris/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome()#service=service_obj)

#-- Firefox
# service_obj = Service("/Users/baris/Desktop/Drivers/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

#-- Edge
# service_obj = Service("/Users/baris/Desktop/Drivers/msedgedriver")
# driver = webdriver.Edge(service=service_obj)




driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
