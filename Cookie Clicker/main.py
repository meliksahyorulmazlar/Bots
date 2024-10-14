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
                    elif "quadrillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 15)
                        prices.append(price)
                    elif "quintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 18)
                        prices.append(price)
                    elif "sextillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 21)
                        prices.append(price)
                    elif "septillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 24)
                        prices.append(price)
                    elif "octillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 27)
                        prices.append(price)
                    elif "nonillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 30)
                        prices.append(price)
                    elif "decillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 33)
                        prices.append(price)
                    elif "undecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 36)
                        prices.append(price)
                    elif "duodecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 39)
                        prices.append(price)
                    elif "tredecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 42)
                        prices.append(price)
                    elif "quattuordecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 45)
                        prices.append(price)
                    elif "quindecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 48)
                        prices.append(price)
                    elif "sexdecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 51)
                        prices.append(price)
                    elif "septendecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 54)
                        prices.append(price)
                    elif "octodecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 57)
                        prices.append(price)
                    elif "novemdecillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 60)
                        prices.append(price)
                    elif "vigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 63)
                        prices.append(price)
                    elif "unvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 66)
                        prices.append(price)
                    elif "duovigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 69)
                        prices.append(price)
                    elif "trevigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 72)
                        prices.append(price)
                    elif "quattuorvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 75)
                        prices.append(price)
                    elif "quinvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 78)
                        prices.append(price)
                    elif "sexvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 81)
                        prices.append(price)
                    elif "septenvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 84)
                        prices.append(price)
                    elif "octovigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 87)
                        prices.append(price)
                    elif "novemvigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 90)
                        prices.append(price)
                    elif "trigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 93)
                        prices.append(price)
                    elif "untrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 96)
                        prices.append(price)
                    elif "duotrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 99)
                        prices.append(price)
                    elif "tretrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 102)
                        prices.append(price)
                    elif "quattuortrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 105)
                        prices.append(price)
                    elif "quintrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 108)
                        prices.append(price)
                    elif "sextrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 111)
                        prices.append(price)
                    elif "septentrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 114)
                        prices.append(price)
                    elif "octotrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 117)
                        prices.append(price)
                    elif "novemtrigintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 120)
                        prices.append(price)
                    elif "quadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 123)
                        prices.append(price)
                    elif "unquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 126)
                        prices.append(price)
                    elif "duoquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 129)
                        prices.append(price)
                    elif "trequadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 132)
                        prices.append(price)
                    elif "quattuorquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 135)
                        prices.append(price)
                    elif "quinquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 138)
                        prices.append(price)
                    elif "sexquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 141)
                        prices.append(price)
                    elif "septenquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 144)
                        prices.append(price)
                    elif "octoquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 147)
                        prices.append(price)
                    elif "novemquadragintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 150)
                        prices.append(price)
                    elif "quinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 153)
                        prices.append(price)
                    elif "unquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 156)
                        prices.append(price)
                    elif "duoquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 159)
                        prices.append(price)
                    elif "trequinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 162)
                        prices.append(price)
                    elif "quattuorquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 165)
                        prices.append(price)
                    elif "quinquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 168)
                        prices.append(price)
                    elif "sexquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 171)
                        prices.append(price)
                    elif "septenquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 174)
                        prices.append(price)
                    elif "octoquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 177)
                        prices.append(price)
                    elif "novemquinquagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 180)
                        prices.append(price)
                    elif "sexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 183)
                        prices.append(price)
                    elif "unsexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 186)
                        prices.append(price)
                    elif "duosexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 189)
                        prices.append(price)
                    elif "tresexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 192)
                        prices.append(price)
                    elif "quattuorsexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 195)
                        prices.append(price)
                    elif "quinsexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 198)
                        prices.append(price)
                    elif "sexsexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 201)
                        prices.append(price)
                    elif "septensexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 204)
                        prices.append(price)
                    elif "octosexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 207)
                        prices.append(price)
                    elif "novemsexagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 210)
                        prices.append(price)
                    elif "septuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 213)
                        prices.append(price)
                    elif "unseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 216)
                        prices.append(price)
                    elif "duoseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 219)
                        prices.append(price)
                    elif "treseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 222)
                        prices.append(price)
                    elif "quattuorseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 225)
                        prices.append(price)
                    elif "quinseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 228)
                        prices.append(price)
                    elif "sexseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 231)
                        prices.append(price)
                    elif "septenseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 234)
                        prices.append(price)
                    elif "octoseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 237)
                        prices.append(price)
                    elif "novemseptuagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 240)
                        prices.append(price)
                    elif "octogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 243)
                        prices.append(price)
                    elif "unoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 246)
                        prices.append(price)
                    elif "duooctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 249)
                        prices.append(price)
                    elif "treoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 252)
                        prices.append(price)
                    elif "quattuoroctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 255)
                        prices.append(price)
                    elif "quinoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 258)
                        prices.append(price)
                    elif "sexoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 261)
                        prices.append(price)
                    elif "septenoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 264)
                        prices.append(price)
                    elif "octooctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 267)
                        prices.append(price)
                    elif "novemoctogintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 270)
                        prices.append(price)
                    elif "nonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 273)
                        prices.append(price)
                    elif "unnonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 276)
                        prices.append(price)
                    elif "duononagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 279)
                        prices.append(price)
                    elif "trenonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 282)
                        prices.append(price)
                    elif "quattuornonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 285)
                        prices.append(price)
                    elif "quinnonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 288)
                        prices.append(price)
                    elif "sexnonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 291)
                        prices.append(price)
                    elif "septennonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 294)
                        prices.append(price)
                    elif "octononagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 297)
                        prices.append(price)
                    elif "novemnonagintillion" in product:
                        price = float(product.split(" ")[0]) * pow(10, 300)
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
