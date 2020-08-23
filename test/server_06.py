import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config

class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web five!!!")


if __name__ == "__main__":
    print("list:", config.options.get("list"))
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    # 实例化一个http服务对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 服务器绑定相应的端口
    httpServer.bind(config.options.get("port"))
    # 开启  多进程
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
    # 把py的config当模块使用
