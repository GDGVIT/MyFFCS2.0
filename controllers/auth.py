from modules import *
class registerHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('signup.html')
