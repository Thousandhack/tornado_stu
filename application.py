from views import index
import tornado.web
import config


class Application(tornado.web.Application):
    """
    相当于路由的功能
    """

    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/test_value", index.TestValueHandler, {"test_value_1": 1, "test_value_2": 2}),  # 传参数进去
            (r"/json", index.JsonHandler),
            (r"/status_code", index.StatusCodeHandler),
            (r"/redirect", index.RedirectHandler),
            # 错误处理
            (r"/is_error", index.ErrorHandler),
            # 反向代理
            tornado.web.url('/rename', index.RenameHandler, name="rename_demo"),
            (r"/one", index.OneHandler),
        ]
        # 把路由给父对象调用
        # **config.settings 为配置
        super(Application, self).__init__(handlers, **config.settings)
