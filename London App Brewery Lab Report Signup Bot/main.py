# London App brewery Lab Report signup

#This code will sign you up for the lab report

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LabReport:
    def __init__(self,name:str,surname:str,email:str):
        self.start_driver()
        name_entry = self.chrome.find_element(By.NAME,"fName")
        name_entry.send_keys(name)
        surname_entry = self.chrome.find_element(By.NAME, "lName")
        surname_entry.send_keys(surname)
        email_entry = self.chrome.find_element(By.NAME, "email")
        email_entry.send_keys(email)

        button = self.chrome.find_element(By.XPATH,'/html/body/form/button')
        button.click()

    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.chrome = webdriver.Chrome(options=chrome_options)
        self.chrome.get(url="http://secure-retreat-92358.herokuapp.com")



if __name__ == "__main__":
    name = "Meliksah"
    surname = "Yorulmazlar"
    email = "yorulk@rpi.edu"
    labreport = LabReport(name=name,surname=surname,email=email)