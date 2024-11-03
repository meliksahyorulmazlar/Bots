import random
import time, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class GitHubBot:
    def __init__(self):
        self.start_driver()
        time.sleep(3)
        self.login()
        self.followers = []
        self.following = []


    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url="https://github.com/login")

    # The following method will log in to GitHub
    def login(self):
        email = os.environ.get("email")
        password = os.environ.get("password")
        email_input = self.driver.find_element(By.NAME, "login")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys(os.environ.get("email"))
        time.sleep(1)
        password_input.send_keys(os.environ.get("password"), Keys.ENTER)
        time.sleep(10)

    # The following bot unfollows accounts for the person's own given page
    # replace meliksahyorulmazlar with the name of your account
    def unfollow(self, number: int):
        page = f"https://github.com/meliksahyorulmazlar?page={number}&tab=following"
        self.driver.get(page)

        paths = []
        path = "#user-profile-frame > div > div:nth-child(1) > div.d-table-cell.col-2.v-align-top.text-right > span > form:nth-child(2) > input.btn.btn-sm"
        for i in range(1, 51):
            replaced = f"div:nth-child({i})"
            new_path = path.replace("div:nth-child(1)", replaced)
            paths.append(new_path)

        for path in paths:
            x = self.driver.find_element(By.CSS_SELECTOR, path)
            x.click()
            time.sleep(0.5)
        time.sleep(5)

    # The following method follows an account when given it's url, and it's page number
    def follow(self, page: str, number: int):
        website = f"{page}?page={number}&tab=followers"
        self.driver.get(website)
        paths = []
        path1 = "#user-profile-frame > div > div:nth-child(1) > div.d-table-cell.col-2.v-align-top.text-right > span > form:nth-child(1) > input.btn.btn-sm"
        path2 = "#user-profile-frame > div > div:nth-child(1) > div.d-table-cell.col-2.v-align-top.text-right > span > form:nth-child(2) > input.btn.btn-sm"
        for i in range(1, 51):
            replaced = f"div:nth-child({i})"
            new_path1 = path1.replace("div:nth-child(1)", replaced)
            new_path2 = path2.replace("div:nth-child(1)", replaced)
            tpl = new_path1, new_path2
            paths.append(tpl)

        for path in paths:
            a = self.driver.find_element(By.CSS_SELECTOR, path[0])
            b = self.driver.find_element(By.CSS_SELECTOR, path[1])
            if a.is_enabled() and a.is_displayed():
                a.click()
            elif b.is_enabled() and b.is_displayed():
                b.click()
            number = random.randint(1,10000)
            t = number/10000
            time.sleep(t)
        time.sleep(2)

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
        for number in range(1,number+1):
            page = f"https://github.com/meliksahyorulmazlar?page={number}&tab=followers"
            self.driver.get(page)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content,'lxml')
            users = [span.text for span in soup.find_all('span',class_='Link--secondary')]
            self.followers += users

    def find_following(self):
        number = 30
        website = f"https://github.com/meliksahyorulmazlar"
        self.driver.get(website)
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')
        links = soup.find_all("a", href=True)
        link = [link.text for link in links if "following" in link['href']]
        link = link[0]
        link = float(link.split("k")[0].strip()) * 1000
        page_count = int((link // 50) + 1)
        possible = f"https://github.com/meliksahyorulmazlar?page={page_count}&tab=following"
        self.driver.get(possible)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        p_tag = soup.find("p", class_="mt-4")
        if p_tag is not None:
            page_count -= 1
        number = page_count
        print(number)
        for number in range(1, number + 1):
            page = f"https://github.com/meliksahyorulmazlar?page={number}&tab=following"
            self.driver.get(page)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'lxml')
            users = [span.text for span in soup.find_all('span', class_='Link--secondary')]
            self.following += users

    def check_accounts(self):
        self.find_followers()
        self.find_following()
        print(self.followers)
        print(len(self.followers))
        print(self.following)
        print(len(self.following))
        accounts = ["IDouble","gamemann",'JohnMwendwa','BEPb','cumsoft','esin','kenjinote','peter-kimanzi','eust-w','OracleBrain','angusshire','Charles-Chrismann','jrohitofficial','george0st','mustafacagri','samarjitsahoo','alineai18','AbdeenM','cusspvz','aplus-developer','ip681','Shehab-Hegab','V1nni00','dalindev','JCSIVO','ethanflower1903',"Nakshatra05",'warmice71','mxmnk','otaviossousa','seniorvuejsdeveloper','mstraughan86','vivekweb2013','Magicianred','JubayerRiyad','MichalPaszkiewicz','mahseema','KevinHock','ValentineFernandes','jeffersonsimaogoncalves','AppServiceProvider','Rodrigo-Cn','jdevfullstack','kulikov-dev','xopaz','dirambora','deepsea514','nikitavoloboev','Gizachew29','AlianeAmaral','decoderwhoami','milsaware','somekindofwallflower']

        random.shuffle(accounts)
        accounts_to_follow = []
        if len(accounts_to_follow) < 500:
            for account in accounts:
                if len(accounts_to_follow) <500:
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
                inputs = self.driver.find_elements(By.TAG_NAME,'input')
                buttons = [inp for inp in inputs if inp.get_attribute('title') == f'Follow {account}']
                if buttons:
                    button = buttons[0]
                    button.click()

if __name__ == "__main__":
    github_bot = GitHubBot()
    github_bot.check_accounts()
