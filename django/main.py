import webapp2

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.write("This is django dir")

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)