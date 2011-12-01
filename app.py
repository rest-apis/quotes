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
    response = ""
    status = "200 OK"
    if environ['REQUEST_METHOD'] == 'GET':
        path = environ['PATH_INFO']
        query_dict = parse_qs(environ['QUERY_STRING'])
        limit = 0
        if 'limit' in query_dict:
            limit = int(query_dict['limit'][0])
        if path == '/quotes':
            quotes = ["%s -- %s"%(quote['content'], quote['author']) for quote in QUOTES]
            if limit:
                response = "\n".join(quotes[:limit])
            else:
                response = "\n".join(quotes)
    else:
        status = "405 Not Allowed"
    response_callback(
        status,
        [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response)))
        ]
    )
    return [response]
daemon = make_server('127.0.0.1', 8000, application)
daemon.serve_forever()
