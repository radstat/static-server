__author__ = 'alay'


from tornado.web import StaticFileHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import os.path

path = os.path.dirname(__file__)


class MyStaticFileHandler(StaticFileHandler):

    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


app = Application([
    (r'/(.*)', MyStaticFileHandler, {'path': path + '/static', 'default_filename': 'index.html'})
])

server = HTTPServer(app)
server.listen(8001, "0.0.0.0")
IOLoop.instance().start()