
from tornado import web
from tornado import httpserver
import tornado.ioloop
from tornado import options


options.define('port',default=8000,type=int)
options.define('list',default=[],type=str,multiple=True)



# 类似与Django中的类试图一样  通过方法进行匹配
class IndexHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('this is for test!')


#  路由
app = web.Application([
    (r'/',IndexHandler)
])


if __name__ == "__main__":
    options.parse_command_line()
    httpserver = httpserver.HTTPServer(app)
    # 使用变量的值
    print(options.options.list)
    httpserver.bind(options.options.port)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()