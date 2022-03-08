import requests

input_list = ["info.cern.ch"]

active_domains = {}

for x in input_list:
    #target="https://"+x

    try:
        response=requests.get(target)
        if "404" not in str(response):
            print("HTTPS version exists",target)
    except:
        target="http://"+x
        response=requests.get(target)
        if "404" not in str():
            print("HTTP version exists",target)    

            
    
        

# print(active_domains)

# file_handle = open("active_domain.txt","w")
# file_handle.write(str(active_domains))

# import os

# input_list = ["cisco.com","google.com","adobe.com","ggsjags.edu"]
# active_domains = {}

# for x in input_list:
#     if "Ping request could not find host" not in str(os.system("ping "+x)):
#         print(x,"Domain is not up")
#     else:
#         active_domains[x] = "Active"

# print(active_domains)
