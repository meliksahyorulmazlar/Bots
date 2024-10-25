#A system that monitors stock prices and identifies significant fluctuations. Upon detecting a notable change(at least 5%), the system automatically retrieves andsends relevant news articles to the user.
#For the stock price change I used Alphavantage (50$ a month but can easily cancel membership)
#For retrieving the news about the stock I used newsapi.org (free)
import requests,datetime,os,smtplib
from email.message import EmailMessage

class StockTradingNews:
    def __init__(self):
        self.tech_companies = [("AAPL", "Apple"), ("MSFT", "Microsoft"), ("AMZN", "Amazon"), ("GOOGL", "Alphabet (Google)"), ("META", "META"), ("NVDA", "NVIDIA"), ("INTC", "Intel"), ("CSCO", "Cisco Systems"), ("ADBE", "Adobe"), ("NFLX", "Netflix"),("TSLA","Tesla"),("ORCL","Oracle")]
        self.financial_companies = [("BRK-A","Berkshire Hathaway"),("JPM", "JPMorgan Chase"), ("BAC", "Bank of America"), ("WFC", "Wells Fargo"),("MS", "Morgan Stanley"), ("GS", "Goldman Sachs"), ("SCHW", "Charles Schwab"),("AXP", "American Express"), ("PNC", "PNC Financial Services"), ("BLK", "BlackRock")]
        self.healthcare_companies = [("JNJ", "Johnson & Johnson"), ("UNH", "UnitedHealth Group"), ("PFE", "Pfizer"),("MRK", "Merck"), ("ABT", "Abbott Laboratories"), ("LLY", "Eli Lilly"),("MDT", "Medtronic"), ("GILD", "Gilead Sciences"), ("ISRG", "Intuitive Surgical"),("CVS", "CVS Health")]
        self.consumer_goods_companies = [("PG", "Procter & Gamble"), ("KO", "Coca-Cola"), ("PEP", "PepsiCo"),("WMT", "Walmart"), ("NKE", "Nike"), ("MCD", "McDonald's"), ("COST", "Costco"),("SBUX", "Starbucks"), ("MO", "Altria"), ("CL", "Colgate-Palmolive")]
        self.energy_companies = [("XOM", "ExxonMobil"), ("CVX", "Chevron"), ("NEE", "NextEra Energy"),("D", "Dominion Energy"), ("DUK", "Duke Energy"), ("SO", "Southern Company"),("PPL", "PPL Corporation"), ("AEP", "American Electric Power"), ("SRE", "Sempra Energy"),("ED", "Consolidated Edison")]
        self.industrial_companies = [("HON", "Honeywell"), ("UNP", "Union Pacific"), ("CAT", "Caterpillar"),("LMT", "Lockheed Martin"), ("UPS", "United Parcel Service"), ("BA", "Boeing"),("RTX", "Raytheon Technologies"), ("DE", "Deere & Company"), ("MMM", "3M"),("GE", "General Electric")]
        self.companies = self.tech_companies + self.financial_companies + self.healthcare_companies + self.consumer_goods_companies + self.energy_companies + self.industrial_companies
        self.dictionary = {"Tech":self.tech_companies,"Finance":self.financial_companies,"Healthcare":self.healthcare_companies,"Consumer Goods":self.consumer_goods_companies,"Industrial":self.industrial_companies}

    #This will show all the categories
    def show_categories(self):
        categories = [key for key in self.dictionary]
        print(categories)

    #This will check a specific category ranging from tech to finance
    def check_industry(self,category:str):
        if category.title() in self.dictionary:
            companies = self.dictionary[category.title()]
            for company in companies:
                self.check_change(company)

    #This will check how much the stock has changed since the previous day
    #If the change is at least 5 percent positive or negative
    #It will find the latest news on the stock and email the user to update the user on the change
    def check_change(self,company:tuple):
        apistockkey = os.environ["apistockkey"]
        symbol = company[0]
        name = company[1]

        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apistockkey}'

        response = requests.get(url=url)

        prices = response.json()['Time Series (Daily)']
        price_list = [(price, prices[price]['4. close']) for price in prices]
        today_price = float(price_list[0][1])
        yesterday_price = float(price_list[1][1])
        print(today_price, yesterday_price, company)
        change = ((today_price - yesterday_price) / yesterday_price) * 100
        if abs(change) >= 5:
            if change >0:
                result = f"{symbol}: 🔺{change:.2f}%"
            else:
                result = f"{symbol}: 🔻{change:.2f}%"
            apinewskey = os.environ["apinewskey"]
            today = datetime.datetime.today()
            one_day = datetime.timedelta(days=1)
            yesterday = today - one_day
            today = today.date()
            yesterday = yesterday.date()

            news = f"https://newsapi.org/v2/everything?q={name}&from={yesterday}&to={yesterday}&sortBy=popularity&apiKey={apinewskey}"
            news_response = requests.get(url=news).json()
            results = news_response["articles"][:3]
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                message = EmailMessage()
                message["From"] = "user@gmail.com"
                message["To"] = "receiver@email.com"
                message["Subject"] = result
                html_message = f"""
                <!DOCTYPE html>
                <html >
                <body>
                    <h1>News:{results[0]["title"]}</h1>
                    <h2>{results[0]["url"]}</h2>
                    <h1>News:{results[1]["title"]}</h1>
                    <h2>{results[1]["url"]}</h2>
                    <h1>News:{results[2]["title"]}</h1>
                    <h2>{results[2]["url"]}</h2>
                </body>
                </html>
                """
                message.add_alternative(html_message, subtype="html")
                connection.starttls()
                connection.login(user="user@gmail.com", password=os.environ["email"])
                connection.send_message(message)
                print(f"Sent:{result}")

    #This will check all the stocks that I have chosen
    def check_all(self):
        for company in self.companies:
            self.check_change(company)




if __name__ == "__main__":
    stn = StockTradingNews()

    #before this code can work,you need to do some things
    #you need to set three environment variables
    #One for stock api called apistockkey
    #One for the newsapi called apinewskey
    #Finally for the password of your email
    #you can get app app passwords for gmail from https://myaccount.google.com/apppasswords
    #you create an app specific password and it can have any name you want
    #then it will give you a 16 character password (The following is an example of how it will look like)
    # abcd efgh ijkl mnop
    #your email environment variable should then be "abcdefghijklmnop"
    #you also need to change who will send the email,and who will receive the email on lines 65,66,83

    #This method will show all the categories/industries to display
    #Takes no input
    #stn.show_categories()

    #This method will check a specific category
    #You can find the categories from stn.show_categories()
    #For example for tech stocks you can say:
    #stn.check_industry(category="Tech")
    #For finance:
    #stn.check_industry(category="Finance")

    #This method will check all the stocks
    #The method takes no input
    #stn.check_all()