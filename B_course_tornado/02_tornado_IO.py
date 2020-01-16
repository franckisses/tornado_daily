

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
    httpserver = httpserver.HTTPServer(app)
    # 监听端口
    httpserver.bind(8888)
    # 启动io复用\
    # 启动多个子进程
    httpserver.start(4)
    # start 参数的取值范围：

    tornado.ioloop.IOLoop.current().start()
"""
    ~tornado.tcpserver.TCPServer.bind`/`~tornado.tcpserver.TCPServer.start`:
       simple multi-process::

            server = HTTPServer(app)
            server.bind(8888)
            server.start(0)  # Forks multiple sub-processes
            IOLoop.current().start()

       When using this interface, an `.IOLoop` must *not* be passed
       to the `HTTPServer` constructor.  `~.TCPServer.start` will always start
       the server on the default singleton `.IOLoop`.
"""