import requests
from Lib.api_login import LoginClass

class CategoryClass:

    def api_addCategory(self, name, type, parentId, orderNum):
        res1 = LoginClass().api_login('dsw12345', '12345678')
        print(res1.cookies['JSESSIONID'])
        HOST = 'http://localhost:8083'
        addCategory_url = f'{HOST}/admin/category/add'
        info = {"name": name, "type": type, "parentId": parentId, "orderNum": orderNum}
        header = {'Content-type': 'application/json'}
        cookie = res1.cookies
        s = cookie['JSESSIONID']
        cookie = {"JSESSIONID": s}
        print(cookie)
        res = requests.post(addCategory_url, json=info, headers=header, cookies=cookie)
        return res


if __name__ == '__main__':

    res = CategoryClass().api_addCategory(3343, 3, 6, 10)
    print(res.text)
