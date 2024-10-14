import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException


class CookieClicker:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.google_driver = webdriver.Chrome(options=chrome_options)
        self.google_driver.get(url="https://orteil.dashnet.org/cookieclicker/")

        cookie_button = self.google_driver.find_element(By.ID, "bigCookie")
        # Time to wait for the website to load
        time.sleep(7)

        # Clicks on the English Language as the language option
        english = self.google_driver.find_element(By.ID, "langSelect-EN")
        english.click()

        # Enters the site
        time.sleep(4)
        store_text = self.google_driver.find_element(By.ID, 'storeTitle')
        store_text.click()
        body = self.google_driver.find_element(By.CSS_SELECTOR, "body")
        for i in range(14):
            body.send_keys(Keys.ARROW_DOWN)
        self.length = 2

    # enter a time interval.
    # suggested 45
    def play(self,time_interval:int):
        while True:
            try:
                t1 = time.time()
                time_passed = False
                while time_passed == False:
                    cookie_button = self.google_driver.find_element(By.ID, "bigCookie")
                    cookie_button.click()
                    t2 = time.time() - t1
                    if t2 > time_interval:
                        time_passed = True
                number_of_cookies = self.google_driver.find_element(By.TAG_NAME, "title").text
                products = self.google_driver.find_elements(By.CLASS_NAME, "price")
                if len(products) != self.length:
                    print("hi")
                    body = self.google_driver.find_element(By.CSS_SELECTOR, "body")
                    amount = len(products) - self.length
                    for i in range(amount * 3):
                        body.send_keys(Keys.ARROW_DOWN)
                    self.length += len(products) - self.length
                products = [product.text.replace(",", "") for product in products if product != " "]
                products = [product for product in products if product != ""]
                prices = []
                for product in products:
                    if "million" in product:
                        price = float(product.split(" ")[0]) * pow(10, 6)
                        prices.append(price)
                    elif "billion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 9)
                        prices.append(price)
                    elif "trillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 9)
                        prices.append(price)
                    else:
                        prices.append(int(product))
                cookies = self.google_driver.find_element(By.CSS_SELECTOR, "#cookies").text
                cookies = int(cookies.split(" ")[0].replace(",", ""))
                # print(cookies)
                # print(products)
                # print(prices)
                while cookies > min(prices):
                    for i in range(len(prices) - 1, -1, -1):
                        if cookies > prices[i]:
                            cookies -= prices[i]
                            link = self.google_driver.find_element(By.ID, f"product{i}")
                            print(link)
                            link.click()
            except (selenium.common.exceptions.StaleElementReferenceException,selenium.common.exceptions.ElementClickInterceptedException,selenium.common.exceptions.ElementNotInteractableException) as e:
                continue

if __name__ == "__main__":
    cc = CookieClicker()
    cc.play(45)