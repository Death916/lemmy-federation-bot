import requests
import time
import datetime

START_TIME = 0
END_TIME = 0

class communities:
    def __init__(self):
        self.url = '/api/v3/community/list/list?type_=Local'
        self.headers = {'Authorization': 'token ' }
        self.page = 1
        self. community_list = []
        self.instance_list = []
        self.limit = 50
        self.total = 0
        self.instance = 0
        self.min_users = 10


    def get_community_list(self):
        page = self.page
        limit=self.limit
        url = self.url + '&page=' + str(page) + '&limit=' + str(limit)
        
      
class instance:
    def __init__(self):
        self.min_users = 50
        self.debug = True
    def get_instances(self):
        url = "https://api.fediverse.observer"

        payload = """
        query {
        nodes (softwarename: "lemmy") {
            domain
            name
            metatitle
            metadescription
            metaimage
            softwarename
            daysmonitored
            monthsmonitored
            date_updated
            date_laststats
            date_created
            countryname
            lat
            long
            uptime_alltime
            latency
            sslexpire
            total_users
            active_users_monthly
            active_users_halfyear
            score
            status
            signup
        }
        }
        """

        response = requests.post(url=url, json={"query": payload})
        data = response.json()
        x=data["data"]["nodes"][3]
        print(data)
        def debug():
            if debug == True:
                for i, node in enumerate(x["data"]["nodes"]):
                    print(f"Node {i}:")
                    print(node["domain"])
                    print(node["name"])
                    print(node["metatitle"])
                    print(node["metadescription"])
                    print("users:" + str(node["total_users"]))
                    print(node["date_created"])
                    print("node number:" + str(i))
                    print("total nodes:" + str(len(x["data"]["nodes"])))


class timer():
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
    
    def start(self):
        self.start_time = datetime.datetime.now()
    
    def end(self):
        self.end_time =datetime.datetime.now()
    
    def elapsed(self):
        print('Duration: {}'.format(self.end_time - self.start_time))
        return str('Duration: {}'.format(self.end_time - self.start_time))
    
    

timer.start()


