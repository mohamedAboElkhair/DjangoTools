import requests


urlpoint  = "http://127.0.0.1:8000/api/produ/1/"
get_response = requests.get(urlpoint)
#print(get_response.headers)
print(get_response.json())
# print(get_response.status_code)