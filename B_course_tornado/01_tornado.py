
from tornado import web
from tornado import httpserver
import tornado.ioloop


# 类似与Django中的类试图一样  通过方法进行匹配
class IndexHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('this is for test!')


#  路由
app = web.Application([
    (r'/',IndexHandler)
])


if __name__ == "__main__":
    # 实例化一个http链接的服务器
    # httpserver = httpserver.HTTPServer(app)
    # 监听端口
    # httpserver.listen(8888)
    # 启动io复用
    # -------------------------------
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()