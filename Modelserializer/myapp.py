import requests 
import json 

url="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)

get_data()
# print(get_data())
# print(get_data(1))

def post_data():
    data={   
        'name':'jackihit',
        'rolls':2,
        'city':'noor'
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)

post_data()
# update

def put_data():
    data={  
        'id':'3',
        'name':'sang',
        
        'city':'ahara'
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)

put_data()

def delete_data():
    data={  
        'id':'2'
    }
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)

# delete_data()
