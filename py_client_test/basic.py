import requests
from getpass import getpass

auth_urlpoint = "http://127.0.0.1:8000/api/auth/"
username = input("what your username?\n")
password = getpass("what your password?\n")
#create token 
auth_ressponse = requests.post(auth_urlpoint,json={'username':username,'password':password})
print(auth_ressponse.json())
if auth_ressponse.status_code == 200:
    token = auth_ressponse.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    urlpoint  = "http://127.0.0.1:8000/api/produ/"
    get_response = requests.get(urlpoint, headers=headers)
    print(get_response.json() )







# urlpoint  = "http://127.0.0.1:8000/api/produ/"
# get_response = requests.get(urlpoint, headers=headers)
# #print(get_response.headers)
# print(get_response.json() )
# # print(get_response.status_code)