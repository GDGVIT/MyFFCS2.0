
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/auth/register",
			auth.registerHandler
		)
]
					