#-*- coding:utf-8 -*-

try:
    from config import BASE_URL
except:
    BASE_URL = 'http://snsapi.ie.cuhk.edu.hk'

def app(environ, start_response):
    rel_url = environ['PATH_INFO'] + '?' + environ['QUERY_STRING']
    import urllib2
    response = urllib2.urlopen(BASE_URL + rel_url)
    status = '200 OK'
    headers = [('Content-type', response.info()['content-type'])]
    start_response(status, headers)
    return [response.read()]

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
