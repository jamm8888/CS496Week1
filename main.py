from google.appengine.api import users
from urlparse import urlparse

import webapp2

class MainPage(webapp2.RequestHanlder):

	def get(self):
		# check if user has an active account session
		user = users.get_current_user()

		# parse the urle and get the url only portion without the query string
		url = urlparse(self.request.uri)
		mainurl = url.scheme + "://" + url.netloc

		# check if the user is logged in, if so display the logged in message
		if user:
			self.response.headers['Content-Type'] = 'text/html; charset = utf-8'
			usergreeting = ('Hello %s!<br><a href="%s">Logout</a>' % 
				(user.nickname(), users.create_logout_url('/')))
			system.response.out.write('<html><body>%s</body></html>' % usergreeting)
		else:		
			self.redirect(users.create_login_url('/'))

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)


