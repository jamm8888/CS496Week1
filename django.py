import webapp2

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.write("This is django dir")
		#print 'this is your guess'

app = webapp2.WSGIApplication([
	('/django', MainPage),
], debug=True)