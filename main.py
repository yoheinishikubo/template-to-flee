import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

def handle_404(request, response, exception):
    response.write('Sorry, nothing at this URL.')
    response.set_status(404)

application = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=False)
application.error_handlers[404] = handle_404
