import requests
import json

URL = 'http://127.0.0.1:8000/aicreate/'

data = {
    'id' : 2,
    'teacher_name' : 'sourav',
    'course_name' : 'english'
}
json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)