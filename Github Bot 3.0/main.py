# GitHub Bot 3.0
# Getting ready for prediction model by gathering data on the users
import os,requests,time,datetime,json,random

class GithubBot:
    def __init__(self):
        self.token = os.environ.get('token')
        self.special = ['GhostOf0days','YangletLiu','Allan-Feng','aalyaz','cshao23','philiplpaterson','connorhakan8','nepthius','enisaras','Hamid-Mofidi','Jshot117','emirkaanozdemr','Chriun','blitzionic','PouyaBaniadam']
        self.headers = {"Authorization": f"Bearer {self.token}","X-GitHub-Api-Version": "2022-11-28"}
        self.blacklist = {}
        self.check_blacklist()
        self.followers = []
        self.following = []
        self.find_followers()
        self.find_following()
        self.automate()

    # I created a blacklist and these users will not be followed again
    def check_blacklist(self):
        try:
            with open('blacklist.json','r') as f:
                self.blacklist:dict = json.load(f)
        except FileNotFoundError:
            pass

    # This method finds all the followers that i follow
    def find_followers(self):
        url = 'https://api.github.com/users/meliksahyorulmazlar/followers'
        page = 1

        self.followers = []
        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            response = requests.get(furl,headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(response.status_code)
                    for item in response.json():
                        self.followers.append(item['login'])
                        print(item['login'],len(self.followers),page)
                    page += 1
            else:
                print(response.status_code)
                print(response.json())
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5-i} seconds left to restart")
                    time.sleep(1)
        print(self.followers)
        print(len(self.followers))

    # This method finds all the people I follow
    def find_following(self):
        url = 'https://api.github.com/users/meliksahyorulmazlar/following'
        page = 1

        self.following = []
        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            response = requests.get(furl,headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(response.status_code)
                    for item in response.json():
                        self.following.append(item['login'])
                        print(item['login'],len(self.following),page)
                    page += 1
            else:
                print(response.status_code)
                print(response.json())
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5-i} seconds left to restart")
                    time.sleep(1)

    # The following method follows one specific GitHub account
    def follow_one_account(self,account:str):
        url = f"https://api.github.com/user/following/{account}"
        response = requests.put(url, headers=self.headers)
        if response.status_code == 204:
            if self.check_your_following(account):
                day = datetime.datetime.now().day
                month = datetime.datetime.now().month
                year = datetime.datetime.now().year
                date_string = f"{day}-{month}-{year}"
                try:
                    with open('following.json','r') as f:
                        following = json.load(f)
                        following[account] = date_string
                    with open('following.json', 'w') as f:
                        json.dump(following,f,indent=4)
                except FileNotFoundError:
                    with open('following.json','w') as f:
                        following = {}
                        following[account] = date_string
                    with open('following.json', 'w') as f:
                        json.dump(following, f, indent=4)
                print(f"Successfully followed {account}!")
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5-i} seconds to restart")
                time.sleep(1)
            self.follow_one_account(account)

    # The following method checks if they are following you or not
    def check_following(self,account:str)->bool:
        url = f"https://api.github.com/users/{account}/following/meliksahyorulmazlar"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.check_following(account)

    # This method checks if you are actually following the account
    # I added this method because there are accounts that the API says that you followed but in reality you did not end up following them
    def check_your_following(self,account:str)->bool:
        url = f"https://api.github.com/users/meliksahyorulmazlar/following/{account}"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.check_following(account)


    # The following method unfollows one specific GitHub account
    def unfollow_one_account(self,account:str):
        url = f"https://api.github.com/user/following/{account}"

        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            with open('following.json','r') as f:
                following:dict = json.load(f)
            date:str = following[account].split("-")
            following.pop(account)
            with open('following.json','w') as f:
                json.dump(following,f,indent=4)

            today = datetime.datetime.now()
            d1_day = int(date[0])
            d1_month = int(date[1])
            d1_year = int(date[2])
            d1 = datetime.datetime(day=d1_day,month=d1_month,year=d1_year)
            d2 = datetime.datetime.now()
            days = (d2-d1).days
            data_dictionary = self.gather_account_data(account)

            if self.check_following(account):
                data_dictionary['result'] = True
                data_dictionary['days_to_follow'] = days
            else:
                data_dictionary['result'] = True
                data_dictionary['days_to_follow'] = -1

            try:
                with open('results.json','r') as f:
                    dictionary = json.load(f)
                with open('results.json','w') as f:
                    dictionary[account] = data_dictionary
                    json.dump(dictionary,f,indent=4)
            except FileNotFoundError:
                with open('results.json','w') as f:
                    json.dump({account:data_dictionary},f,indent=4)

            print(f"Successfully unfollowed {account}!")
        else:
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.unfollow_one_account(account)

    # This method unfollows accounts that have followed us back or accounts that have not followed us back for 7 days and puts them in a blacklist
    def unfollow_accounts(self):
        self.find_followers()
        with open('following.json','r') as f:
            following:dict = json.load(f)

        for account in following:
            if account not in self.special:
                if account in self.followers:
                    time.sleep(1)
                    self.unfollow_one_account(account)
                else:
                    date_string = following[account].split("-")
                    d1_day = int(date_string[0])
                    d1_month = int(date_string[1])
                    d1_year = int(date_string[2])
                    d1 = datetime.datetime(day=d1_day,month=d1_month,year=d1_year)
                    d2 = datetime.datetime.now()
                    days = (d2-d1).days
                    if days >= 7:
                        time.sleep(1)
                        self.unfollow_one_account(account)
                        d2_day = d2.day
                        d2_month = d2.month
                        d2_year = d2.year
                        today_string = f"{d2_day}-{d2_month}-{d2_year}"
                        try:
                            with open('blacklist.json','r') as f:
                                blacklist = json.load(f)
                                blacklist[account] = today_string
                            with open('blacklist.json','w') as f:
                                json.dump(blacklist,f,indent=4)
                        except FileNotFoundError:
                            with open('blacklist.json','w') as f:
                                json.dump({account:today_string},f,indent=4)

    # Gathers data on the user
    def gather_account_data(self,account:str) -> dict:
        url = f"https://api.github.com/users/{account}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            dictionary = {}
            dictionary['name'] = account
            dictionary['creation_date'] = data['created_at'].split("T")[0]
            dictionary['update_date'] = data['updated_at'].split("T")[0]
            dictionary['followers'] = data['followers']
            dictionary['following'] = data['following']
            ratio = None
            if data['following'] == 0:
                ratio = data['followers']/1
            else:
                ratio = data['followers']/data['following']
            dictionary['ratio'] = ratio
            dictionary['repo_count'] = data['public_repos']

            if data['twitter_username'] is None:
                dictionary['twitter'] = False
            else:
                dictionary['twitter'] = True

            if data['bio'] is None:
                dictionary['bio'] = False
            else:
                dictionary['bio'] = True

            if data['email'] is None:
                dictionary['email'] = False
            else:
                dictionary['email'] = True

            if data['location'] is None:
                dictionary['location'] = False
            else:
                dictionary['location'] = True
            print(dictionary)
            return dictionary
        else:
            time.sleep(5)
            print(f"Error: {response.status_code}")
            print('Time to give a break')
            for i in range(5):
                print(f"{i} seconds.{5 - i} seconds to restart")
                time.sleep(1)
            self.gather_account_data(account)

    # The following method follows accounts
    def follow_accounts(self):
        choices= ["IDouble","gamemann",'JohnMwendwa','BEPb','cumsoft','esin','kenjinote','peter-kimanzi','eust-w','OracleBrain','angusshire','Charles-Chrismann','jrohitofficial','george0st','mustafacagri','samarjitsahoo','alineai18','AbdeenM','cusspvz','aplus-developer','ip681','Shehab-Hegab','V1nni00','dalindev','JCSIVO','ethanflower1903',"Nakshatra05",'warmice71','mxmnk','otaviossousa','seniorvuejsdeveloper','mstraughan86','vivekweb2013','Magicianred','JubayerRiyad','MichalPaszkiewicz','mahseema','KevinHock','ValentineFernandes','jeffersonsimaogoncalves','AppServiceProvider','Rodrigo-Cn','jdevfullstack','kulikov-dev','xopaz','dirambora','deepsea514','nikitavoloboev','Gizachew29','AlianeAmaral','decoderwhoami','milsaware','somekindofwallflower']

        account_chosen = random.choice(choices)
        print(account_chosen)
        accounts = []
        url = f'https://api.github.com/users/{account_chosen}/followers'
        page = 1

        loop = True
        while loop:
            furl = f"{url}?page={page}&per_page=100"
            response = requests.get(furl, headers=self.headers)

            if response.status_code == 200:
                if response.json() == []:
                    loop = False
                else:
                    print(response.status_code)
                    for item in response.json():
                        accounts.append(item['login'])
                        print(item['login'], len(accounts), page)
                    page += 1
            else:
                print(response.status_code)
                print(response.json())
                print('Time to give a break')
                for i in range(5):
                    print(f"{i} seconds, {5 - i} seconds left to restart")
                    time.sleep(1)

        count = 0
        for account in accounts:
            if account not in self.blacklist:
                if account not in self.special:
                    if account not in self.following:
                        if account not in self.followers:
                            if count != 500:
                                time.sleep(1)
                                self.follow_one_account(account)
                                if self.check_your_following(account):
                                    count += 1


    # This method automates the entire process on repeat
    def automate(self):
        while True:
            t1 = time.time()
            self.follow_accounts()
            self.unfollow_accounts()

            loop = True
            while loop:

                t2 = time.time()
                if t2 - t1 >3600:
                    loop = False
                else:
                    print(f"{t2-t1} seconds have gone by. {3600-t1} seconds left.")
                    time.sleep(2)

if __name__ == "__main__":
    bot = GithubBot()


