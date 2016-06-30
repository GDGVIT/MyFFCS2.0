from modules import *

class timeTableHandler(RequestHandler):
	@coroutine
	@removeslash
	def get(self):
		if bool(self.get_secure_cookie('user')):
			userInfo = None
			userNameInfo = None
			current_id = self.get_secure_cookie("user")
			userInfo = yield db.users.find_one({'_id' : ObjectId(current_id)})
			self.render('home.html',result = dict(userInfo=userInfo))
		else:
			self.redirect('/auth/register')