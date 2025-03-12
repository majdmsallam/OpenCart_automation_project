import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self,endpoint,params=None, headers=None):
        return self.session.get(f'{self.base_url}{endpoint}', params=params,headers=headers)

    def post(self,endpoint, data=None, json=None, headers=None):
        return self.session.post(f'{self.base_url}{endpoint}', data=data, json=json, headers=headers)

    def put(self,endpoint, data=None, json=None, headers=None):
        return self.session.put(f'{self.base_url}{endpoint}', data=data, json=json, headers=headers)

    def delete(self,endpoint,data=None,json=None, headers=None):
        return self.session.delete(f'{self.base_url}{endpoint}', json=json,data=data, headers=headers)