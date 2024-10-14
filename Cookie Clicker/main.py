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

    def convert_cookies(self, text):
        if "million" in text:
            return float(text.split("\n")[0]) * pow(10, 6)
        elif "billion" in text:
            return float(text.split("\n")[0]) * pow(10, 9)
        elif "trillion" in text:
            return float(text.split("\n")[0]) * pow(10, 12)
        elif "quadrillion" in text:
            return float(text.split("\n")[0]) * pow(10, 15)
        elif "quintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 18)
        elif "sextillion" in text:
            return float(text.split("\n")[0]) * pow(10, 21)
        elif "septillion" in text:
            return float(text.split("\n")[0]) * pow(10, 24)
        elif "octillion" in text:
            return float(text.split("\n")[0]) * pow(10, 27)
        elif "nonillion" in text:
            return float(text.split("\n")[0]) * pow(10, 30)
        elif "decillion" in text:
            return float(text.split("\n")[0]) * pow(10, 33)
        elif "undecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 36)
        elif "duodecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 39)
        elif "tredecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 42)
        elif "quattuordecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 45)
        elif "quindecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 48)
        elif "sexdecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 51)
        elif "septendecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 54)
        elif "octodecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 57)
        elif "novemdecillion" in text:
            return float(text.split("\n")[0]) * pow(10, 60)
        elif "vigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 63)
        elif "unvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 66)
        elif "duovigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 69)
        elif "trevigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 72)
        elif "quattuorvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 75)
        elif "quinvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 78)
        elif "sexvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 81)
        elif "septenvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 84)
        elif "octovigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 87)
        elif "novemvigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 90)
        elif "trigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 93)
        elif "untrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 96)
        elif "duotrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 99)
        elif "tretrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 102)
        elif "quattuortrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 105)
        elif "quintrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 108)
        elif "sextrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 111)
        elif "septentrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 114)
        elif "octotrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 117)
        elif "novemtrigintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 120)
        elif "quadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 123)
        elif "unquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 126)
        elif "duoquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 129)
        elif "trequadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 132)
        elif "quattuorquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 135)
        elif "quinquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 138)
        elif "sexquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 141)
        elif "septenquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 144)
        elif "octoquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 147)
        elif "novemquadragintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 150)
        elif "quinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 153)
        elif "unquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 156)
        elif "duoquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 159)
        elif "trequinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 162)
        elif "quattuorquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 165)
        elif "quinquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 168)
        elif "sexquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 171)
        elif "septenquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 174)
        elif "octoquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 177)
        elif "novemquinquagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 180)
        elif "sexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 183)
        elif "unsexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 186)
        elif "duosexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 189)
        elif "tresexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 192)
        elif "quattuorsexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 195)
        elif "quinsexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 198)
        elif "sexsexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 201)
        elif "septensexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 204)
        elif "octosexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 207)
        elif "novemsexagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 210)
        elif "septuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 213)
        elif "unseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 216)
        elif "duoseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 219)
        elif "treseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 222)
        elif "quattuorseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 225)
        elif "quinseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 228)
        elif "sexseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 231)
        elif "septenseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 234)
        elif "octoseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 237)
        elif "novemseptuagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 240)
        elif "octogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 243)
        elif "unoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 246)
        elif "duooctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 249)
        elif "treoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 252)
        elif "quattuoroctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 255)
        elif "quinoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 258)
        elif "sexoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 261)
        elif "septenoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 264)
        elif "octooctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 267)
        elif "novemoctogintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 270)
        elif "nonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 273)
        elif "unnonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 276)
        elif "duononagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 279)
        elif "trenonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 282)
        elif "quattuornonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 285)
        elif "quinnonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 288)
        elif "sexnonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 291)
        elif "septennonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 294)
        elif "octononagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 297)
        elif "novemnonagintillion" in text:
            return float(text.split("\n")[0]) * pow(10, 300)
        elif "centillion" in text:
            return float(text.split("\n")[0]) * pow(10, 303)
        else:
            print([text])
            return int(text.split("\n")[0].replace(",", "").replace(" cookies",''))

    def convert_large_numbers(self,text):
        if "million" in text:
            return float(text.split(" ")[0]) * pow(10, 6)
        elif "billion" in text:
            return float(text.split(" ")[0]) * pow(10, 9)
        elif "trillion" in text:
            return float(text.split(" ")[0]) * pow(10, 12)
        elif "quadrillion" in text:
            return float(text.split(" ")[0]) * pow(10, 15)
        elif "quintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 18)
        elif "sextillion" in text:
            return float(text.split(" ")[0]) * pow(10, 21)
        elif "septillion" in text:
            return float(text.split(" ")[0]) * pow(10, 24)
        elif "octillion" in text:
            return float(text.split(" ")[0]) * pow(10, 27)
        elif "nonillion" in text:
            return float(text.split(" ")[0]) * pow(10, 30)
        elif "decillion" in text:
            return float(text.split(" ")[0]) * pow(10, 33)
        elif "undecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 36)
        elif "duodecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 39)
        elif "tredecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 42)
        elif "quattuordecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 45)
        elif "quindecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 48)
        elif "sexdecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 51)
        elif "septendecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 54)
        elif "octodecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 57)
        elif "novemdecillion" in text:
            return float(text.split(" ")[0]) * pow(10, 60)
        elif "vigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 63)
        elif "unvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 66)
        elif "duovigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 69)
        elif "trevigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 72)
        elif "quattuorvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 75)
        elif "quinvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 78)
        elif "sexvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 81)
        elif "septenvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 84)
        elif "octovigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 87)
        elif "novemvigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 90)
        elif "trigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 93)
        elif "untrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 96)
        elif "duotrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 99)
        elif "tretrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 102)
        elif "quattuortrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 105)
        elif "quintrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 108)
        elif "sextrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 111)
        elif "septentrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 114)
        elif "octotrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 117)
        elif "novemtrigintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 120)
        elif "quadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 123)
        elif "unquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 126)
        elif "duoquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 129)
        elif "trequadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 132)
        elif "quattuorquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 135)
        elif "quinquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 138)
        elif "sexquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 141)
        elif "septenquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 144)
        elif "octoquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 147)
        elif "novemquadragintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 150)
        elif "quinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 153)
        elif "unquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 156)
        elif "duoquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 159)
        elif "trequinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 162)
        elif "quattuorquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 165)
        elif "quinquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 168)
        elif "sexquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 171)
        elif "septenquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 174)
        elif "octoquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 177)
        elif "novemquinquagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 180)
        elif "sexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 183)
        elif "unsexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 186)
        elif "duosexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 189)
        elif "tresexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 192)
        elif "quattuorsexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 195)
        elif "quinsexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 198)
        elif "sexsexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 201)
        elif "septensexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 204)
        elif "octosexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 207)
        elif "novemsexagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 210)
        elif "septuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 213)
        elif "unseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 216)
        elif "duoseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 219)
        elif "treseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 222)
        elif "quattuorseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 225)
        elif "quinseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 228)
        elif "sexseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 231)
        elif "septenseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 234)
        elif "octoseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 237)
        elif "novemseptuagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 240)
        elif "octogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 243)
        elif "unoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 246)
        elif "duooctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 249)
        elif "treoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 252)
        elif "quattuoroctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 255)
        elif "quinoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 258)
        elif "sexoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 261)
        elif "septenoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 264)
        elif "octooctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 267)
        elif "novemoctogintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 270)
        elif "nonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 273)
        elif "unnonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 276)
        elif "duononagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 279)
        elif "trenonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 282)
        elif "quattuornonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 285)
        elif "quinnonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 288)
        elif "sexnonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 291)
        elif "septennonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 294)
        elif "octononagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 297)
        elif "novemnonagintillion" in text:
            return float(text.split(" ")[0]) * pow(10, 300)
        elif "centillion" in text:
            return float(text.split(" ")[0]) * pow(10, 303)
        else:
            print([text])
            return int(text.split("\n")[0].replace(",", "").replace(" cookies",''))

    # enter a time interval.
    # suggested 45
    def play(self):
        time_interval = 5
        while True:
            print(time_interval)
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
                    body = self.google_driver.find_element(By.CSS_SELECTOR, "body")
                    amount = len(products) - self.length
                    for i in range(amount * 3):
                        body.send_keys(Keys.ARROW_DOWN)
                    self.length += len(products) - self.length
                products = [product.text.replace(",", "") for product in products if product != " "]
                products = [product for product in products if product != ""]
                prices = []
                for product in products:
                    price = self.convert_large_numbers(product)
                    prices.append(price)
                cookies = self.google_driver.find_element(By.CSS_SELECTOR, "#cookies").text
                cookies = self.convert_cookies(cookies)
                # print(cookies)
                # print(products)
                # print(prices)
                while cookies > min(prices):
                    for i in range(len(prices) - 1, -1, -1):
                        if cookies > prices[i]:
                            cookies -= prices[i]
                            link = self.google_driver.find_element(By.ID, f"product{i}")
                            link.click()
            except (selenium.common.exceptions.StaleElementReferenceException,selenium.common.exceptions.ElementClickInterceptedException,selenium.common.exceptions.ElementNotInteractableException) as e:
                continue
            finally:
                time_interval += 1

if __name__ == "__main__":
    cc = CookieClicker()
    cc.play()
