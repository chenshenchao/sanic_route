from sanic import Sanic
from sanic.response import json
from sanic_route import attach
from example import controller

app = Sanic("sanic_route_debug_app")

# 注册整个模块内被 @http_* 装饰器标记的路由
attach(app, controller)

@app.route('/')
async def test(request):
    '''
    原本的 sanic 路由
    '''
    
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run()