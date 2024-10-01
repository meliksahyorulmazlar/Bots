import time, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GitHubBot:
    def __init__(self):
        self.start_driver()
        time.sleep(3)
        self.login()

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
        time.sleep(5)


if __name__ == "__main__":
    github_bot = GitHubBot()





