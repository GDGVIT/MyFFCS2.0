from modules import *
class logoutHandler(SentryMixin,RequestHandler):
	@removeslash
	@coroutine
	def get(self):
		self.clear_cookie('user')
		self.redirect('/?loggedOut=true')
