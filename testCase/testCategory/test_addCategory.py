import pytest
import json
from Lib.api_login import LoginClass
from Lib.api_addCategory import CategoryClass


class TestCategory:
    def setup_class(self):
        res = LoginClass().api_login('dsw12345', '12345678').cookies



    def test_add_success(self,res):
        test_data = {"name": "123", "type":3, "parentId":6, "orderNum":10 }
        CategoryClass().api_addCategory(res, test_data)