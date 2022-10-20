from sanic.response import json
from sanic_route import http_get

@http_get('/example.html')
async def index(request):

    return json({'hello': 'world'})