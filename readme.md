# [sanic_route](https://github.com/chenshenchao/sanic_route)

扩展了 Sanic 的路由装饰器，使得通过一次注册就加载整个模块包括其子模块内全部被 @http_* 装饰的处理器。

## 使用和示例

```bash
# 通过 pip 安装
pip install sanic_route
```

### 示例

示例结构如下，通过执行 python demo.py 来启动示例。

```
demo.py
example
  |- __init__.py
  |- controller
        |- __init__.py
        |- bar.py
        |- foo.py
```

```python
# demo.py

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
```

```python
# example/controller/__init__.py
# 注册了 /example.html 的路由。
from sanic.response import json
from sanic_route import http_get

@http_get('/example.html')
async def index(request):

    return json({'hello': 'world'})
```

```python
# example/controller/bar.py
# 注册了 /bar/index.html 和 /bar/info/<bid:int>' 的路由。
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
```

```python
# example/controller/foo.py
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
```

## 开发与发布

注：如果要扩展本库，可以 fork 后添加自己的修改。

```bash
# 安装 setup.py 依赖的库。
pip install ran

# 安装本地的本库进环境 用于调试。
pip install -e . -i https://pypi.python.org/pypi

# 安装发布打包的工具。
pip install twine wheel

# 打包
python setup.py sdist bdist_wheel

# 上传
twine upload dist/*

# 发布后可以指定源更新，这样可以测试发布后的效果。
pip install --upgrade suoran -i https://pypi.python.org/pypi
```