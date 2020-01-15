from tornado import ioloop,web,httpserver


class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write('欢迎来到我的博客网站')
        self.render('./index.html')


class CreateDailyHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write('欢迎来到我的博客网站1')
        self.render('./create.html')

    def post(self,*args,**kwargs):
        weahter = self.get_argument('weather ')

        mood = self.get_argument('mood')
        content = self.get_argument('content')
        print(weahter,mood,content)



application = web.Application([
    (r'/',MainPageHandler),
    (r'/create',CreateDailyHandler),

])

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.current().start()