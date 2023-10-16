# API 示例
from bottle import get, post, delete, run, template

counters = 0

@get('/api/v1/hello/<name>')
def greet(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/v1/count')
def cnt():
    global counters
    return {'count': counters, 'description': 'Operation Count'}

@post('/api/v1/add/<a:int>/<b:int>')
def add(a, b):
    global counters
    counters += 1
    return {'result': a + b, 
            'status': 'OK', 
            'description': 'A+B Problem',
            }

@delete('/api/v1/delete/<user>')
def user_delete(user):
    global counters
    counters += 1
    return {'result': 'OK', 
            'description': 'Delete User: {}'.format(user),
            }


run(host='localhost', port=8088)