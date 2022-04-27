import requests

class HttpMethod:

    def get(url: str, params: dict = None, headers: dict = None) -> requests.Response:
        try:
            return requests.get(url= url, params= params, headers= headers)
        except Exception as err:
            print(err)

    def post(url: str, headers: dict = None, data: dict = None) -> requests.Response:
        try:
            return requests.post(url= url, data= data, headers= headers)
        except Exception as err:
            print(err)

    def put(url: str, headers: dict = None, data: dict = None) -> requests.Response:
        try:
            return requests.put(url= url, data= data, headers= headers)
        except Exception as err:
            print(err)