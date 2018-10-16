import requests
import json


url = "http://localhost:5000/api/v1"
data = {
    "website": "random",
    "keyword": "nana"
}

r = requests.post(url, data=data)

with open("result.txt", "w+") as fw:
    fw.write(r.text)
    fw.close()