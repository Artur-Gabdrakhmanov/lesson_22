from config import Hosts
from utils.base_session import BaseSession


class DemoQaWithEnv:
    def __init__(self, env):
        self.demoqa = BaseSession(url=Hosts(env).demoqa)
        self.reqres = BaseSession(url=Hosts(env).reqres)

    def login(self, email, password):
        return self.demoqa.post(
            url="/login",
            params={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )

    def add_product_to_cart(self):
        self.demoqa.post("addproducttocart/catalog/31/1/1")


    @property
    def session_reqres(self):
        return self.reqres
