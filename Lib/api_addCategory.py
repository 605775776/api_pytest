import requests
import json

class CategoryClass:

    def api_addCategory(self, cookie, test_data):
        HOST = 'http://localhost:8083'
        addCategory_url = f'{HOST}/admin/category/add'
        header = {'Content-type': 'application/json'}
        res = requests.post(addCategory_url, json=test_data, headers=header, cookies=cookie)
        return json.loads(res)
