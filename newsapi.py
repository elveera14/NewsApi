import requests, json
from exceptions import InvalidRequest

_api_endpoints = {
    'top-headlines':"https://newsapi.org/v2/top-headlines",
    'everything':"https://newsapi.org/v2/everything",
    'sources':"https://newsapi.org/v2/sources",
}

class NewsApi:

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    def connect(self, endpoint, params, pagesize=10, page=1):
        url = _api_endpoints.get(endpoint) + '?apiKey='+ '0eacfb62485f4a4cacf8b62680452532'
        para_list = ''
        for key in params:
            para_list += (key + '=' + params[key])
        if para_list:
            url = url + '&' + para_list
        try:
            response = requests.get(url=url)
            if not response:
                raise InvalidRequest('Invalid Request')
        except InvalidRequest as e:
            print(e.message)
            return
        return response.json()
     
    