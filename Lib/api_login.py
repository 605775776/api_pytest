import requests
import config

class LoginClass:
    def api_login(self, username, password):
        login_url = f'{config.HOST}/login'
        info = {'username': username, 'password': password}
        header = {'Content-type' : 'application/x-www-form-urlencoded'}
        res = requests.post(login_url, data=info, headers=header)
        return res

if __name__ == '__main__':
    res = LoginClass().api_login('dsw12345', '12345678')
    print(res.text)
