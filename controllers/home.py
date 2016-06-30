
'''
Preset controller by torn for / route
'''
from modules import *
class homeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Welcome to MyFFCS. <a href = "/auth/register">Go to app</a>')
					