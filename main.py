import datetime
import webapp2

class MainPage(webapp2.RequestHandler):

	def get(self):
		message = '<p>The current time is: <b>%s</b></p>' % datetime.datetime.now()
		self.response.out.write(message)

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)


