import requests
import config

class RegisterClass:
    def api_register(self, username, password):
        register_url = f'{config.HOST}/register'
        info = {'username': username, 'password': password}
        header = {'Content-type' : 'application/x-www-form-urlencoded'}
        res = requests.post(register_url, data=info, headers=header)
        return res

if __name__ == '__main__':
    res = RegisterClass().api_register('dsw12345', '12345678')
    print(res.text)
