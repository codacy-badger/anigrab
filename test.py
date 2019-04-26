import requests
import json


url = "http://anigrab.herokuapp.com/api/v1"
data = {
    "website": "random",
    "keyword": "nanatsu"
}

r = requests.post(url, data=data)

with open("result.txt", "w+") as fw:
    fw.write(r.text)
    fw.close()
