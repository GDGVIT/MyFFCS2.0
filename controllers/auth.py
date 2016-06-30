from modules import *
class registerHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('signup.html')

	@coroutine
	@removeslash
	def post(self):
		regno = self.get_argument('regno','')
		password = self.get_argument('password','')
		name = self.get_argument('name','')
		userData = {
		'regno' : regno,
		'password' : password,
		'name' : name
		}
		if(regno!="" and password != ""):
			result = yield db.users.find_one({'regno':regno})
			if bool(result):
				self.redirect('/auth/register?username=taken')
			else:
				result = yield db.users.insert(userData)
				self.set_secure_cookie('user',str(result['_id']))
				self.redirect('/home')

class loginHandler(RequestHandler):
	@coroutine
	@removeslash
	def post(self):
		regno = self.get_argument('regno','')
		password = self.get_argument('password','')
		if(regno!="" and password != ""):
			result = yield db.users.find_one({'$and':[{'password':password},{'regno':regno}]})
		if bool(result):
			self.set_secure_cookie("user", str(result['_id']))
			self.render('/home', result=dict(userInfo=result))
		else:
			self.redirect("/auth/register?status=False")

