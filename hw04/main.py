import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, m):
        '''/m_row'''

        m=str(m)

        c='n'

        if c in m:
            m=9

        m=int (m)
        
        

        html='''
        <html>
        <body>
        <table>
        '''
        self.write(html)
        
        for a in range(1,m+1):
            html = '<TR>'+html+'<TR>'
            for b in range(1,a+1):
                html += '<TD>%d*%d=%d</TD>'% (a,b,a*b)
            html += '</TR>'+html+'</TR>'
        
        self.write(html)

        html = '''
        </table>
        </body>
        </html>
        '''
        
        self.write(html)
        

application = tornado.web.Application([
    (r"(?:/(\S))?", MainHandler),
],debug=True)


        

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
