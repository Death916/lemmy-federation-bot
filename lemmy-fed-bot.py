import requests
import time
import datetime
import os
import json


START_TIME = 0
END_TIME = 0
DEBUG = True
class communities:
    def __init__(self, instance_list):
        self.url = '/api/v3/community/list?type_=Local'
        self.headers = {'Authorization': 'token ' }
        self.page = "1"
        self. community_list = []
        self.instance_list = instance_list
        
        self.total = 0
        self.instance = 0
        self.min_users = 10


    def get_community_list(self):
        instance_list = self.instance_list
        limit=self.limit
        
        for i in instance_list:
            instance_domain = i['domain']
            combined_url ="https://" +  str(instance_domain) + self.url + '&page' + self.page + '&limit=' + str(limit)
            print(combined_url)
            x = requests.get(combined_url)
            print(x)
            if x.status_code == 200:
                 self.community_list = []
                 self.community_list.append(i)
                 self.total = len(self.community_list)
                 self.page = str(int(self.page) + 1)
                 
                 print("total communities found: " + self.total)
            else:
             print("Error: " + str(x.status_code))
             continue
        

        
        
      
class instance:
    def __init__(self):
        self.min_users = 50
        

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
            signup
        }
        }
        """

        response = requests.post(url=url, json={"query": payload})
        instance_data = response.json()
       
        filtered_json_data = []
        for i,  entry in enumerate(instance_data["data"]["nodes"]):
            if entry['total_users'] >= 50:
                filtered_json_data.append(entry)
        open('debug.json', 'w')
        json.dump(filtered_json_data, open('debug.json', 'w'))
        return filtered_json_data


        



class sub_chooser():
    def __init__(self):
        self.min_users = 50
        self.debug = True
        self.instance_name = ""
        self.community_name = ""
        




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
                    instances = instance()
                    filtered_json_data = instances.get_instances()
                    open('debug.json', 'w')
                    json.dump(filtered_json_data, open('debug.json', 'w'))
                # remove instances with less than 50 users
             
                counter = 0
                for i in (filtered_json_data):  
                    counter = counter + 1
                    #print(f"Node {i}:")
                    print('domain: ' + i['domain'])
                    print("name: " + i["name"])
                    print("metatitle: " + str(i["metatitle"])) 
                    print("metadescription: " + str(i["metadescription"]))
                    print("users: " + str(i["total_users"])) 
                    print("date_created: " + i["date_created"])
                    checked_instances = []                     
                    print("total nodes: " + str(len(filtered_json_data)))
                    checked_instances.append(i['domain'])
                    print("node number: " + str(counter))
                
                communitiy_list = communities(filtered_json_data)
                communitiy_list.get_community_list()

                 

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
    

