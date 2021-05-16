import requests as requests
from django.core.exceptions import PermissionDenied


class ProxyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        proxy = Proxy()
        if proxy.validar_token(request):
            return self.get_response(request)
        else:
            raise PermissionDenied('Operação não permitida')



class Proxy():
    def validar_token(self, request):
        headers = {}
        url = 'http://pizzaria-fasam.herokuapp.com/validar-token/'
        headers['Authorization'] = f'JWT {request.headers["Authorization"]}'
        result = requests.get(url, headers=headers)

        return result.status_code == 200
