
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn

from motor import MotorClient
from routes import *

db = MotorClient('mongodb://gdgvit:baapbaaphotahain@ds011495.mlab.com:11495/myffcs')['myffcs']
settings = dict(
		template_path = os.path.join(os.path.dirname(__file__), "views"),
		static_path = os.path.join(os.path.dirname(__file__), "static"),
		debug=torn.Debug(),
		db=db,
		cookie_secret="35an18y3-u12u-7n10-4gf1-232g23ce04n6",
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(torn.Port())
	IOLoop.current().start()

					