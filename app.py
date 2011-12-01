from cgi import parse_qs
from wsgiref.simple_server import make_server
QUOTES = [
    {'author': '' , 'content': ''},
    {'author': '' , 'content': ''},
    {'author': '' , 'content': ''},
    {'author': '' , 'content': ''},
    {'author': '' , 'content': ''},
    {'author': '' , 'content': ''}
]

def application(environ, response_callback):
    #El querystring viene en environ['QUERY_STRING'], la ruta, en environ['PATH_INFO'] 
    #y el accept, en environ['HTTP_ACCEPT']
    resp = "Hola mundo"
    response_callback(
        "200 OK",
        [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(resp)))
        ]
    )
    return [resp]
daemon = make_server('127.0.0.1', 8000, application)
daemon.serve_forever()
