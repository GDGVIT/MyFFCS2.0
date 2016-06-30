
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/auth/register",
			auth.registerHandler
		),
		(
			r"/logout",
			logout.logoutHandler
		),
		(
			r"/home",
			timetable.timeTableHandler
		),
		(
			r"/auth/login",
			auth.loginHandler
		)
]
					