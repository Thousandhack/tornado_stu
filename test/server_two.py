import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web!!!")


if __name__ == "__main__":
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    # 实例化一个http服务对象  单进程
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
