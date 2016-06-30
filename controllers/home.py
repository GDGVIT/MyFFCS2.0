
'''
Preset controller by torn for / route
'''
from modules import *
class homeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Welcome to Tornado Application')
					