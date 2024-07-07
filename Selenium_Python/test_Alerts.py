import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = webdriver.Chrome()
        name = "Vishal"
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
        driver.find_element(By.ID, "alertbtn").click()
        alert = driver.switch_to.alert
        alertText = alert.text
        print(alertText)
        assert name in alertText
        alert.accept()
        # alert.dismiss()


if __name__ == '__main__':
    unittest.main()
