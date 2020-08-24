from views.index import IndexHandler
import tornado.web


class Application(tornado.web.Application):
    """
    相当于路由的功能
    """

    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]
        # 把路由给父对象调用
        super(Application, self).__init__(handlers)
