from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if ''not in [a,b]:
	a,b = int(a),int(b)
	out = open('/var/www/html/txt/result.txt','w')
	out.write("add :" + str(a+b) + "\n")
	out.write("multiply :" + str(a*b) )
	out.close()
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
