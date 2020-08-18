import tornado.web
import tornado.ioloop

"""
tornado 基础的web框架模块
tornado 核心IO的循环模块
封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
"""


# 类比django的视图，业务处理类
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web!!!")


if __name__ == "__main__":
    # 实例化应用的对象
    # 使用Application类进行实例化，tornado web框架的应用核心
    # 是与服务器对应的接口
    # 里面保存了路由映射表

    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    # listen 用于创建http的实例，并绑定端口
    # 只能在单进程模式中使用
    app.listen(8800)
    # http://127.0.0.1:8800/
    # 返回：hello tornado web!!!
    """
    IOLoop.current()
    返回当前线程的IOLoop实例
    start() 启动IO实例循环
    """
    tornado.ioloop.IOLoop.current().start()
