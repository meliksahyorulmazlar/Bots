# Tinder like / reject bot

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class TinderBot:
    def __init__(self):
        self.start_driver()
        time.sleep(90)


    # The following method will start the selenium webdriver
    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url='https://tinder.com')

    # The following method will reject the user
    def reject(self):
        try:
            body = self.driver.find_element(By.CSS_SELECTOR,"body")
            body.send_keys(Keys.ARROW_LEFT)
            time.sleep(1)  # Adjust sleep time to control the speed
        except Exception as e:
            print(f"Error swiping: {e}")
            time.sleep(2)

    #The following method will like the user
    def like(self):
        try:
            body = self.driver.find_element(By.CSS_SELECTOR,"body")
            body.send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)  # Adjust sleep time to control the speed
        except Exception as e:
            print(f"Error swiping: {e}")
            time.sleep(2)


if __name__ == "__main__":
    tb = TinderBot()
    for i in range(50):
        tb.like()