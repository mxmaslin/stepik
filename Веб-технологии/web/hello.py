def application(environ, start_response):
    data = environ['QUERY_STRING']
    d = '\n'.join(str(data).split('&'))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([d])