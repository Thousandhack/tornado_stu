import tornado.ioloop
import tornado.httpserver
import tornado.options
from application import Application
import config

if __name__ == "__main__":
    app = Application()
    # 实例化一个http服务对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 服务器绑定相应的端口
    httpServer.bind(config.options.get("port"))
    # 开启  多进程
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
