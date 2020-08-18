import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web three!!!")


if __name__ == "__main__":
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    # 实例化一个http服务对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 服务器绑定相应的端口
    httpServer.bind(8000)
    # 开启  多进程
    httpServer.start(5)
    # 值可以不写或None或负数，这些都认为开启服务器对于的cpu核心数
    # 虽然提供了多进程的方式，但是有问题，不建议上面的方式启动多进程
    # 使用手动启动多个进程，并可以绑定不能的端口
    # 有问题：
    # （1）每个子进程都会从父进程中复制中一份IOloop的实例，如果在创建子进程前修改IOLoop, 会影响子进程。
    # （2）所有的进程都是由一个命令启动的，无法做到在不停止服务的情况下修改代码。
    # （3）所有进程共享一个端口，想要分别监控很困难。
    tornado.ioloop.IOLoop.current().start()

