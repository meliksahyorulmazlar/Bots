# import os
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import requests,lxml
# from bs4 import BeautifulSoup
#
#
# class TargetBot:
#     def __init__(self):
#         self.start_driver()
#         self.sign_in()
#         self.check()
#         self.buy()
#
#
#     def start_driver(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_experimental_option("detach",True)
#
#         self.driver = webdriver.Chrome(options=chrome_options)
#
#
#     def sign_in(self):
#         self.driver.get(url='https://www.target.com')
#         time.sleep(2)
#
#         spans = [span for span in self.driver.find_elements(By.TAG_NAME,'span') if span.text == "Sign in"]
#
#         for span in spans:
#             print(span.text)
#
#         spans[0].click()
#         time.sleep(2)
#
#         buttons = [button for button in self.driver.find_elements(By.TAG_NAME, 'button') if button.text == "Sign in"]
#
#         for button in buttons:
#             print(button.text)
#
#         buttons[0].click()
#
#         time.sleep(2)
#         email = self.driver.find_element(By.NAME,'username')
#         password = self.driver.find_element(By.NAME,'password')
#         email.send_keys(os.environ.get('email'))
#         password.send_keys(os.environ.get('password',Keys.ENTER))
#
#         items = [span for span in self.driver.find_elements(By.TAG_NAME,'span') if span.text == 'Sign in with password']
#
#         time.sleep(1)
#         for item in items:
#             print(item.text)
#
#         items[0].click()
#         time.sleep(3)
#
#     def check(self):
#         time.sleep(1)
#
#         #the first one is the one to buy
#         #page = 'https://www.target.com/p/pokemon-trading-card-game-sword-38-shield-lost-origin-elite-trainer-box/-/A-87154260'
#         page = 'https://www.target.com/p/pokemon-trading-card-game-grand-adventure-collection/-/A-92698332'
#         boolean = True
#         while boolean:
#             self.driver.get(page)
#             self.driver.execute_script("window.scrollBy(0, 500);")
#             time.sleep(15)
#             buttons = [b for b in self.driver.find_elements(By.TAG_NAME,'button') if b.text== 'Qty\n1']
#             print(buttons)
#             time.sleep(5)
#
#             if buttons:
#                 buttons[0].click()
#
#                 time.sleep(0.5)
#                 amounts = [div for div in self.driver.find_elements(By.TAG_NAME,'div') if div.text == '3']
#                 amounts[0].click()
#
#                 time.sleep(0.5)
#                 buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Add to cart']
#                 buttons[0].click()
#                 boolean = False
#
#     def buy(self):
#         time.sleep(5)
#         self.driver.get(url='https://www.target.com/cart')
#
#         time.sleep(1)
#         buttons = [b for b in self.driver.find_elements(By.TAG_NAME,'button') if b.text == 'Check out']
#         buttons[0].click()
#
# if __name__ == "__main__":
#     tb = TargetBot()

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests,lxml
from bs4 import BeautifulSoup


class TargetBot:
    def __init__(self):
        self.start_driver()
        self.sign_in()
        self.check()
        self.buy()



    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.driver = webdriver.Chrome(options=chrome_options)


    def sign_in(self):
        self.driver.get(url='https://www.target.com')
        time.sleep(2)

        spans = [span for span in self.driver.find_elements(By.TAG_NAME,'span') if span.text == "Sign in"]

        for span in spans:
            print(span.text)

        spans[0].click()
        time.sleep(2)

        buttons = [button for button in self.driver.find_elements(By.TAG_NAME, 'button') if button.text == "Sign in"]

        for button in buttons:
            print(button.text)

        buttons[0].click()

        time.sleep(2)
        email = self.driver.find_element(By.NAME,'username')
        password = self.driver.find_element(By.NAME,'password')
        email.send_keys(os.environ.get('email'))
        password.send_keys(os.environ.get('password',Keys.ENTER))

        items = [span for span in self.driver.find_elements(By.TAG_NAME,'span') if span.text == 'Sign in with password']

        time.sleep(1)
        for item in items:
            print(item.text)

        items[0].click()
        time.sleep(2)

    def check(self):
        #the first one is the one to buy
        page = 'https://www.target.com/p/pokemon-trading-card-game-sword-38-shield-lost-origin-elite-trainer-box/-/A-87154260'
        page = 'https://www.target.com/p/pokemon-trading-card-game-grand-adventure-collection/-/A-92698332'
        # page = 'https://www.target.com/p/ocean-spray-whole-berry-cranberry-sauce-14oz/-/A-12936068#lnk=sametab'
        page = 'https://www.target.com/p/grossmos-flying-dino-assortment-interactive-green/-/A-90996598#lnk=sametab'
        boolean = True
        while boolean:
            self.driver.get(page)
            self.driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1.5)

            spans = [span for span in self.driver.find_elements(By.TAG_NAME,'span') if span.text == 'Shipping']
            if spans:
                spans[0].click()
                buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Qty\n1']
                if buttons:
                    print(buttons)
                    buttons[0].click()

                    time.sleep(0.2)
                    amounts = [div for div in self.driver.find_elements(By.TAG_NAME,'div') if div.text == '3']
                    amounts[0].click()

                    time.sleep(0.2)
                    buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Add to cart']
                    buttons[0].click()
                    boolean = False
                    break
            else:
                buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Qty\n1']
                if buttons:
                    print(buttons)
                    buttons[0].click()

                    time.sleep(0.01)
                    amounts = [div for div in self.driver.find_elements(By.TAG_NAME, 'div') if div.text == '3']
                    amounts[0].click()

                    time.sleep(0.01)
                    buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Add to cart']
                    buttons[0].click()
                    boolean = False
                    break
                else:
                    time.sleep(20)




    def buy(self):
        self.driver.get(url='https://www.target.com/cart')

        time.sleep(2)
        buttons = [b for b in self.driver.find_elements(By.TAG_NAME,'button') if 'Check out' in b.text]
        buttons[0].click()

        time.sleep(2)

        button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/button')

        button.click()

        time.sleep(0.2)
        cvv = "693"
        cvv_selector = self.driver.find_element(By.XPATH,'/html/body/div[11]/div/div/div[2]/div[2]/div[1]/input')
        cvv_selector.send_keys(cvv)

        confirm = self.driver.find_element(By.XPATH,'/html/body/div[11]/div/div/div[2]/div[2]/button')
        confirm.click()




if __name__ == "__main__":
    tb = TargetBot()


 # scrollable_div = self.driver.find_element(By.TAG_NAME, "h2")
                #
                # Scroll up by 100 pixels
                # for i in range(10):
                #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 100", scrollable_div)
                #
                # buttons = [b for b in self.driver.find_elements(By.TAG_NAME, 'button') if b.text == 'Place your order']
                # buttons[0].click()
