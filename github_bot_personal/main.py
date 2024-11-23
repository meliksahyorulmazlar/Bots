import random,datetime
import time, os,json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class GitHubBot:
    def __init__(self):
        #self.login()
        self.special = {'GhostOf0days': {'day': 9, 'month': 8, 'year': 2023}, 'YangletLiu': {'day': 9, 'month': 8, 'year': 2023}, 'Chriun': {'day': 9, 'month': 8, 'year': 2023}, 'Allan-Feng': {'day': 9, 'month': 8, 'year': 2023}, 'aalyaz': {'day': 9, 'month': 8, 'year': 2023}, 'cshao23': {'day': 9, 'month': 8, 'year': 2023}, 'philiplpaterson': {'day': 9, 'month': 8, 'year': 2023}, 'connorhakan8': {'day': 9, 'month': 8, 'year': 2023}, 'nepthius': {'day': 9, 'month': 8, 'year': 2023}, 'enisaras': {'day': 9, 'month': 8, 'year': 2023}, 'Hamid-Mofidi': {'day': 9, 'month': 8, 'year': 2023}, 'Jshot117': {'day': 9, 'month': 8, 'year': 2023}, 'emirkaanozdemr': {'day': 9, 'month': 8, 'year': 2023}}
        self.followers = []
        self.following = {}
        self.login()


    def find_following(self):
        with open("following.json",'r') as f:
            self.following = json.load(f)


    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url="https://github.com/login")
        time.sleep(3)

    def login(self):
        self.start_driver()
        email = os.environ.get("email")
        password = os.environ.get("password")
        email_input = self.driver.find_element(By.NAME, "login")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys(os.environ.get("email"))
        time.sleep(1)
        password_input.send_keys(os.environ.get("password"), Keys.ENTER)
        time.sleep(10)

    def find_followers(self):
        website = f"https://github.com/meliksahyorulmazlar"
        self.driver.get(website)
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')
        links = soup.find_all("a", href=True)
        link = [link.text for link in links if "followers" in link['href']]
        link = link[0]
        link = float(link.split("k")[0].strip()) * 1000
        page_count = int((link // 50) + 1)
        possible = f"https://github.com/meliksahyorulmazlar?page={page_count}&tab=followers"
        self.driver.get(possible)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        p_tag = soup.find("p", class_="mt-4")
        if p_tag is not None:
            page_count -= 1
        number = page_count
        print(number)
        for number in range(1, number + 1):
            page = f"https://github.com/meliksahyorulmazlar?page={number}&tab=followers"
            self.driver.get(page)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'lxml')
            users = [span.text for span in soup.find_all('span', class_='Link--secondary')]
            self.followers += users

    def check_accounts(self):
        self.find_followers()
        self.find_following()
        accounts = ["IDouble", "gamemann", 'JohnMwendwa', 'BEPb', 'cumsoft', 'esin', 'kenjinote', 'peter-kimanzi','eust-w', 'OracleBrain', 'angusshire', 'Charles-Chrismann', 'jrohitofficial', 'george0st','mustafacagri', 'samarjitsahoo', 'alineai18', 'AbdeenM', 'cusspvz', 'aplus-developer', 'ip681','Shehab-Hegab', 'V1nni00', 'dalindev', 'JCSIVO', 'ethanflower1903', "Nakshatra05", 'warmice71','mxmnk', 'otaviossousa', 'seniorvuejsdeveloper', 'mstraughan86', 'vivekweb2013', 'Magicianred','JubayerRiyad', 'MichalPaszkiewicz', 'mahseema', 'KevinHock', 'ValentineFernandes','jeffersonsimaogoncalves', 'AppServiceProvider', 'Rodrigo-Cn', 'jdevfullstack', 'kulikov-dev','xopaz', 'dirambora', 'deepsea514', 'nikitavoloboev', 'Gizachew29', 'AlianeAmaral', 'decoderwhoami','milsaware', 'somekindofwallflower']

        random.shuffle(accounts)
        accounts_to_follow = []
        if len(accounts_to_follow) < 500:
            for account in accounts:
                if len(accounts_to_follow) < 500:
                    website = f"https://github.com/{account}"
                    self.driver.get(website)
                    html_content = self.driver.page_source
                    soup = BeautifulSoup(html_content, 'lxml')
                    links = soup.find_all("a", href=True)
                    link = [link.text for link in links if "followers" in link['href']]
                    link = link[0]
                    link = float(link.split("k")[0].strip()) * 1000
                    page_count = int((link // 50) + 1)
                    possible = f"https://github.com/{account}?page={page_count}&tab=followers"
                    self.driver.get(possible)
                    soup = BeautifulSoup(self.driver.page_source, 'lxml')
                    p_tag = soup.find("p", class_="mt-4")
                    if p_tag is not None:
                        page_count -= 1
                    number = page_count
                    for number in range(1, number + 1):
                        if len(accounts_to_follow) < 500:
                            page = f"https://github.com/{account}?page={number}&tab=followers"
                            self.driver.get(page)
                            html_content = self.driver.page_source
                            soup = BeautifulSoup(html_content, 'lxml')
                            users = [span.text for span in soup.find_all('span', class_='Link--secondary')]
                            if len(accounts_to_follow) < 500:
                                for user in users:
                                    if len(accounts_to_follow) < 500:
                                        if user not in self.followers and user not in self.following:
                                            accounts_to_follow.append(user)
                                            print(user, len(accounts_to_follow))
        for account in accounts_to_follow:
            if account not in self.following and not account in self.followers:
                user_page = f"https://github.com/{account}"
                self.driver.get(user_page)
                inputs = self.driver.find_elements(By.TAG_NAME, 'input')
                buttons = [inp for inp in inputs if inp.get_attribute('title') == f'Follow {account}']
                if buttons:
                    button = buttons[0]
                    button.click()
                    day = datetime.datetime.now().day
                    month = datetime.datetime.now().month
                    year = datetime.datetime.now().year
                    self.following[account] = {'day': day, 'month': month, 'year': year}
                    with open("following.json",'w') as f:
                        json.dump(self.following,f,ensure_ascii=False,indent=4)

    def unfollow_account(self, account: str):
        user_page = f"https://github.com/{account}"
        self.driver.get(user_page)
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        buttons = [inp for inp in inputs if inp.get_attribute('title') == f'Unfollow {account}']
        if buttons:
            button = buttons[0]
            button.click()
            self.following.pop(account)
            with open('following.json', 'w') as f:
                json.dump(self.following, f, ensure_ascii=False, indent=4)

    def unfollow_followed_ones(self):
        self.followers = []
        self.following = {}
        self.find_followers()
        self.find_following()

        accounts = [account for account in self.following if account in self.followers]
        for account in accounts:
            if account not in self.special:
                self.unfollow_account(account)
                self.following.pop(account)
                with open('following.json','w') as f:
                    json.dump(self.following,f,ensure_ascii=False,indent=4)



    def unfollow_following(self):
        self.following = {}
        self.find_following()
        d1 = datetime.datetime.now()

        for account in self.following:
            if account not in self.special:
                day1 = self.following[account]['day']
                month1 = self.following[account]['month']
                year1 = self.following[account]['year']
                d2 = datetime.datetime(day=day1,month=month1,year=year1)
                days = (d1-d2).days
                if days >= 3:
                    self.unfollow_account(account)

    def automate(self):
        while True:
            t1 = time.time()
            self.followers = []
            self.following = {}
            self.find_following()
            self.find_followers()
            self.check_accounts()
            self.unfollow_followed_ones()
            self.unfollow_following()


            new_loop = True
            while new_loop:
                t2 = time.time()
                if t2 - t1 >= 3600:
                    new_loop = False

if __name__ == "__main__":
    github_bot = GitHubBot()
    github_bot.automate()
