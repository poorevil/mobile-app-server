import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import db

from vo.Message import Message

class MainPage(webapp.RequestHandler):
    
    def get(self):
        msgs = Message.gql('order by date desc')
        
        self.response.out.write('''
            <html>
            <head>
                <meta charset="utf-8" />
                <title>Untitled</title>
            </head>
            <body>
            <table>
            ''')
        
        for msg in msgs:
            self.response.out.write('<tr><td>%s</td><td>%s</td></tr>'%(cgi.escape(msg.content),msg.date))
        
        self.response.out.write('''
            </table>
                <form action="/sign" method="post">
                    <div><textarea name="content" rows="3" cols="60"></textarea></div>
                    <div><input type="submit" value="Sign Guestbook"></div>
                </form>
            </body>
            </html>
            ''')
    
class Sign(webapp.RequestHandler):
    def post(self):
        msg = Message()
        msg.content = self.request.get('content')
        
        msg.put()
        
        self.redirect('/')

application = webapp.WSGIApplication([('/', MainPage), ('/sign', Sign)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
