__author__ = 'alay'


from tornado.web import StaticFileHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler
import os

path = os.path.dirname(__file__)

static_path = path + '/static'
if not os.path.isdir(static_path):
    os.mkdir(static_path)


class MyStaticFileHandler(StaticFileHandler):

    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        url = 'http://' + self.request.headers['Host'] + '/app'
        self.redirect(url)

app = Application([
    (r'/', IndexHandler),
    (r'/(.*)', MyStaticFileHandler, {'path': static_path, 'default_filename': 'index.html'})
])

server = HTTPServer(app)
server.listen(8001, "0.0.0.0")
IOLoop.instance().start()