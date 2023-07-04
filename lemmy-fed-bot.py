import requests
import time
import datetime
import os
import json
from plemmy import LemmyHttp


START_TIME = 0
END_TIME = 0
DEBUG = True
RATE_LIMIT = 3
class communities:
    def __init__(self, instance_list):
        self.url = '/api/v3/community/list?type_=Local'
        self.headers = {'Authorization': 'token ' }
        self.page = "1"
        self. community_list = []
        self.instance_list = instance_list
        self.limit = 50 #amount of results per page
        self.total = 0
        self.instance = 0
        self.min_users = 10
        self.site_captcha_enabled = []


    def get_community_list(self,):
        instance_list = self.instance_list
        limit=self.limit
        
           #TODO: REMOVE OR CLEANUP THIS DEBUG

        if DEBUG == True:
            instance_domain = "lemmy.death916.xyz"
            combined_url ="https://" +  str(instance_domain) + self.url + '&page' + self.page + '&limit=' + str(limit)
            print(combined_url)
        
            response= requests.get(combined_url)
            print(response)
            print(response.json())
            community_json = response.json()
            
            
            if response.status_code == 200:
                self.community_list.append(community_json)
                self.total = len(self.community_list)

                # write to file
                with open('community_list.json', 'w') as f:
                    json.dump(self.community_list, f)
                for i in community_json['communities']:
                   print(i['community']['name'])
                   print(i['community']['id'])
               
            else:
                print(x.status_code)
                print(x.text)
                
        else:
            for i in instance_list:

                instance_domain = i['domain']
                combined_url ="https://" +  str(instance_domain) + self.url + '&page' + self.page + '&limit=' + str(limit)
                print(combined_url)
        
                try:
                    x = requests.get(combined_url)
                    print(x)
                    if x.status_code == 200:
                        self.community_list.append(i)
                        self.total = len(self.community_list)
                        self.page = str(int(self.page) + 1)
                        
                        print("total communities found: " + str(self.total))

                except Exception as e:
                                print(e)
                                print("error getting community list")
                                continue
                                
    def parse_community_list(self, community_json):
         for i in community_json['communities']:
                   print(i['community']['name'])

         

        
class instance:
    def __init__(self, debug, **kwargs):
        self.min_users = kwargs['min_users']
        self.debug = DEBUG
        
        

    # get_instance_list
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
            signupz
        }
        }
        """
        if self.debug  and os.path.exists('./debug.json'):
            pass
        else:
            response = requests.post(url=url, json={"query": payload})
            instance_data = response.json()
       
            filtered_json_data = []
            for i,  entry in enumerate(instance_data["data"]["nodes"]):
                if entry['active_users_monthly'] >= self.min_users and entry['status'] == 1:
                    filtered_json_data.append(entry)
      
            open('debug.json', 'w')
            json.dump(filtered_json_data, open('debug.json', 'w'))
            return filtered_json_data
'''''
class user(self, instance, username, password,):
     def __init__(self,  **kwargs):
          self.username = kwargs['username']
          self.password = kwargs['password']
       
     def login(self):
          password = self.password
          username = self.username
'''
   
        


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
    
    



def debug():
            
                print('---------------debugging ------------')
              #check if instance file exists
                if os.path.exists('./debug.json'):
                    instance_json = open('debug.json', 'r')
                    filtered_json_data = json.load(instance_json)
                else:
                    instances = instance(DEBUG, min_users=1)
                    filtered_json_data = instances.get_instances()
                    open('debug.json', 'w')
                    json.dump(filtered_json_data, open('debug.json', 'w'))
                
             
                counter = 0
                for i in (filtered_json_data):  
                    counter = counter + 1
                    #print(f"Node {i}:")
                    print('domain: ' + i['domain'])
                    print("name: " + i["name"])
                    print("metatitle: " + str(i["metatitle"])) 
                    print("metadescription: " + str(i["metadescription"]))
                    print("active users: " + str(i["active_users_monthly"])) 
                    print("date_created: " + i["date_created"])
                    checked_instances = []                     
                    print("total nodes: " + str(len(filtered_json_data)))
                    checked_instances.append(i['domain'])
                    print("node number: " + str(counter))
                
                communitiy_list = communities(filtered_json_data)
                communitiy_list.get_community_list()

                follow = LemmyHttp('https://lemmy.death916.xyz')
                username = input("enter admin username: ")
                password = input("enter admin password: ")
                follow.login(username, password)
                follow.follow_community
                 

                print('---------------end debugging ------------')   

def main():
    timers = timer()
    timers.start()
    if DEBUG == True:
        debug()
        timers.end()
        timers.elapsed()
    else:

        instance_data = instance()
        instance_data = instance_data.get_instances()
     

if __name__ == "__main__":
    main()
    

