from sanic.response import json
from sanic_route import http_get

class BarController:
    '''
    '''
    
    @http_get('/bar/index.json')
    async def index(self, request):
        '''
        
        '''
        page = request.args.get('p', [1])[0]
        return json({'bar': 'index', 'page': page })

    @http_get('/bar/info/<bid:(\d+).json>')
    async def info(self, request, bid):
        return json({'bar': bid})