import requests
import json

URL="http://127.0.0.1:8000/stulist"

r=requests.get(URL)

data=r.json()




if __name__ == "__main__":
    print(data)