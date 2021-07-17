from Lib.api_login import LoginClass
import json

class TestUser:
    def test_login_success(self):
        res = json.loads(LoginClass().api_login('dsw12345', '12345678'))
        assert res['status'] == 10000
        assert res['msg'] == 'SUCCESS'

    def test_login_no_password(self):
        res = json.loads(LoginClass().api_login('dsw12345', ''))
        assert res['msg'] == '密码不能为空'

    def test_login_error_password(self):
        res = json.loads(LoginClass().api_login('dsw12345', '123'))
        assert res['msg'] == '密码错误'

