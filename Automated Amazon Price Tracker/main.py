# Automated Amazon Price Tracker


import time,lxml,json
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

class AmazonPriceTracker:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        self.start_json()
        self.start_driver()
        self.graphics()

    #The following method will initiate the json files
    def start_json(self):
        try:
            with open("data.json","r") as f:
                self.link_data = json.load(f)
        except FileNotFoundError:
            with open("data.json","w") as f:
                self.link_data = {}
                json.dump({},f)

    # This method will initiate the Selenium webdriver
    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.google_driver = webdriver.Chrome(options=chrome_options)
        self.google_driver.get(url="https://www.amazon.com")


    # The following method will start the graphics
    def graphics(self):
        self.root = Tk()
        self.root.minsize(width=500,height=300)
        self.root.maxsize(width=500,height=300)
        self.root.title("Automated Amazon Price Tracker")

        self.link_label = Label(self.root,text="Amazon Link:")
        self.link_label.place(x=75,y=100)
        self.link_label.focus()

        self.link_entry = Entry(self.root,width=27)
        self.link_entry.place(x=200,y=100)

        self.price_label = Label(self.root,text="Expected Price:")
        self.price_label.place(x=75,y=150)

        self.price_entry = Entry(self.root,width=27)
        self.price_entry.place(x=200,y=150)


        self.enter_button = Button(self.root,text="Enter",command=self.find_price)
        self.enter_button.place(x=200,y=200)

        self.root.mainloop()

    # This method will find the price of the amazon product
    def find_price(self):
        product = self.link_entry.get()
        expected_price_entry = self.price_entry.get()
        expected_price = float(expected_price_entry)


        if len(product) == 0 or len(expected_price_entry) == 0:
            messagebox.showerror(message="Something is missing")
        else:
            if product in self.link_data:
                messagebox.showinfo(message=f"The product was previously searched for.\nThe price was ${self.link_data[product]}")
                time.sleep(5)
            price = self.return_product_price(amazon_link=product)
            change = ((expected_price - price) / (price)) * 100

            if price < expected_price:
                messagebox.showinfo(
                    message=f"The price is ${price}.\nIt is below the expected the price of ${expected_price}.\nPrice change:{change:.2f}%")
            elif price > expected_price:
                messagebox.showinfo(
                    message=f"The price is ${price}.\nIt is above the expected the price of ${expected_price}.\nPrice change:{change:.2f}%")
            else:
                messagebox.showinfo(message="The price has not changed")


            new_data = {product: price}
            self.link_data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(self.link_data, f)

            self.link_entry.delete(0,END)
            self.price_entry.delete(0,END)
            self.google_driver.get(url="https://www.amazon.com")


    #This method will go to amazon and retrieve the product's price as a float
    def return_product_price(self,amazon_link:str)->float:
        self.google_driver.get(url=amazon_link)

        soup = BeautifulSoup(self.google_driver.page_source,"lxml")

        price = soup.find("span",class_="a-offscreen")

        price = price.text.strip("$")

        price = float(price)

        return price



if __name__ == "__main__":
    apt = AmazonPriceTracker()



