from sanic.response import json
from sanic_route import http_any, http_delete, http_post, http_put

class FooController:
    '''
    
    '''

    @http_post('/foo/post')
    async def index(self, request):
        '''
        
        '''

        return json({'foo': 'post' })

    @http_any('/foo/any')
    async def request_any(self, request):
        '''
        
        '''
        
        return json({'foo': 'any' })

    @http_delete('/foo/delete/<fid:int>')
    async def delete_one(self, request, fid):
        '''
        
        '''

        return json({'foo': 'delete', 'fid': fid })

    @http_put('/foo/put')
    async def put_one(self, request):
        '''
        
        '''

        return json({ 'foo': 'put' })

    

