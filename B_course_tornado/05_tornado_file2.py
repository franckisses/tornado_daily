
from tornado import web
from tornado import httpserver
import tornado.ioloop
from tornado import options
import config


# 类似与Django中的类试图一样  通过方法进行匹配
class IndexHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('this is for test!')


#  路由
app = web.Application([
    (r'/',IndexHandler)
])


if __name__ == "__main__":
    httpserver = httpserver.HTTPServer(app)
    # 使用变量的值
    print(config.options['list'])
    httpserver.bind(config.options['port'])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()