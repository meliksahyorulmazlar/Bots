# Internet Speed Twitter Bot
# This bot will get the person's internet speed etc. and post it on Twitter


import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import messagebox



class InternetTwitterBot:
    def __init__(self):
        key = os.environ['password']
        print(key)
        self.start_chrome()
        # This way the graphical user interface only comes up when the internet speed website has loaded up
        self.start_graphics()
        self.tweet()

    # The following method initiates the selenium webdriver
    def start_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach',True)
        self.chrome = webdriver.Chrome(options=chrome_options)

    # This method initiates the graphics
    def start_graphics(self):
        self.root = Tk()
        self.root.title("Internet Speed Twitter Bot")
        self.root.minsize(width=600,height=400)
        self.root.maxsize(width=600,height=400)

        self.username_label = Label(self.root,text="Username:")
        self.username_label.place(x=75,y=100)

        self.username_entry = Entry(self.root,width=40)
        self.username_entry.place(x=150,y=100)

        self.username_entry.focus()

        self.username_tip = Label(self.root,text="For the username, enter your phone number, username or your email")
        self.username_tip.place(x=75,y=130)

        self.password_label = Label(self.root,text="Password:")
        self.password_label.place(x=75,y=180)

        self.password_entry = Entry(self.root, width=40)
        self.password_entry.place(x=150, y=180)

        self.password_tip = Label(self.root,text="For the password, enter your password")
        self.password_tip.place(x=75,y=210)

        self.enter_button = Button(self.root,text="Enter",width=40,command=self.process)
        self.enter_button.place(x=100,y=270)

        self.root.mainloop()

    # This method will check if both a username and a password has been entered to initiate the process of tweeting the internet speed
    def process(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0:
            messagebox.showerror(message="Something is missing")
        else:
            self.username = username
            self.password = password
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)

            self.username_entry.update_idletasks()
            self.password_entry.update_idletasks()

            self.root.after(100, self.get_internet_speed)
            self.root.after(200, self.tweet)

    # The following method will retrieve the download speed in mbps, the upload speed in mbps and the ping in ms
    def get_internet_speed(self):
        self.chrome.get(url="https://www.speedtest.net")
        go = self.chrome.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()

        time.sleep(60)

        upload = self.chrome.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        download = self.chrome.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')


        ping = self.chrome.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span')

        self.upload_speed = float(upload.text)

        self.download_speed = float(download.text)

        self.ping = int(ping.text)

    # The following method will tweet the following:
    # The download speed,the upload speed and the ping
    def tweet(self):

        self.chrome.get(url="https://x.com/i/flow/login")

        time.sleep(5)
        username_entry = self.chrome.find_element(By.NAME,'text')
        username_entry.send_keys(self.username,Keys.ENTER)

        time.sleep(1)
        password_entry = self.chrome.find_element(By.NAME,'password')
        password_entry.send_keys(self.password,Keys.ENTER)
        time.sleep(2)
        print(self.chrome.current_url)
        if self.chrome.current_url == "https://x.com/i/flow/login?redirect_after_login=%2Fcompose%2Fpost":
            time.sleep(5)
            username_entry = self.chrome.find_element(By.NAME, 'text')
            username_entry.send_keys(self.username, Keys.ENTER)

            time.sleep(1)
            password_entry = self.chrome.find_element(By.NAME, 'password')
            password_entry.send_keys(self.password, Keys.ENTER)

        self.chrome.get(url="https://x.com/compose/post")

        time.sleep(1)
        tweet = self.chrome.find_element(By.CSS_SELECTOR,'div[contenteditable="true"]')

        message = f"The Download speed is {self.download_speed} mbps.The Upload speed is {self.upload_speed} mbps.The Ping is {self.ping} ms"
        tweet.send_keys(message)

        spans = self.chrome.find_elements(By.TAG_NAME,"span")

        span_element = None
        clickable = [span for span in spans if span.text == "Post"]
        print(clickable)
        for span in clickable:
            span.click()


if __name__ == "__main__":
    twitter = InternetTwitterBot()
