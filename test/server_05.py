import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int)
tornado.options.define("list", default=[], type=str, multiple=True)


class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web five!!!")


if __name__ == "__main__":
    # 将取出打印日志的配置文件
    # tornado.options.options.logging = None
    # options.parse_config_file(path, final=final)
    tornado.options.parse_config_file("config")
    print("list:", tornado.options.options.list)
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    # 实例化一个http服务对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 服务器绑定相应的端口
    httpServer.bind(tornado.options.options.port)
    # 开启  多进程
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

    # 从配置文件导入参数
    # tornado.options.config.file(path)
