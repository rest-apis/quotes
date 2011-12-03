from cgi import parse_qs
from wsgiref.simple_server import make_server

QUOTES = [
    {'author': 'Ken Thompson' , 'content': 'When in doubt, use brute force'},
    {'author': 'Brian W. Kernighan' , 'content': 'The most effective debugging tool is still careful thought, coupled with judiciously placed print statements'},
    {'author': 'E.W. Dijkstra' , 'content': 'Simplicity is prerequisite for reliability'},
    {'author': 'E.W. Dijkstra' , 'content': "The computing scientist's main challenge is not to get confused by the complexities of his own making"},
    {'author': 'Ken Thompson' , 'content': 'One of my most productive days was throwing away 1000 lines of code'},
    {'author': 'Jeff Sickel' , 'content': 'Deleted code is debugged code'}
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
