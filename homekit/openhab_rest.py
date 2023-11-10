import requests


url = "http://{ip}:8080/rest/items/HomeKitPythonRest"
headers = {'Content-Type': 'text/plain', 'Accept':'application/json'}

def post_oh_homekit_item(event):       
        print("The Array is: ", event)
        r = requests.post(url, json={'item': '{aid}.{iid}'.format(aid=event[0], iid=event[1]), 'value':event[2]}, headers=headers)
        print(r.text)