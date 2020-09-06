from views import index
import tornado.web
import config
import os
from conn_sql import ConnectSql


class Application(tornado.web.Application):
    """
    相当于路由的功能
    """

    def __init__(self):
        handlers = [
            (r"/return", index.IndexReturnHandler),
            (r"/test_value", index.TestValueHandler, {"test_value_1": 1, "test_value_2": 2}),  # 传参数进去
            (r"/json", index.JsonHandler),
            (r"/status_code", index.StatusCodeHandler),
            (r"/redirect", index.RedirectHandler),
            # 错误处理
            (r"/is_error", index.ErrorHandler),
            # 反向代理  name 值不变，/ rename可以随意变化 [少用]
            tornado.web.url('/rename', index.RenameHandler, name="rename_demo"),
            (r"/one", index.OneHandler),
            # 获取参数
            # (r"/request_value/(\w+)/(\w+)", index.RequestVlaueHandler),
            # 加这个?P<demo_01> 在handler 不需要排序
            (r"/request_value/(?P<demo_02>\w+)/(?P<demo_01>\w+)", index.RequestVlaueHandler),
            # post方法
            (r"/request_value", index.RequestPostVlaueHandler),
            # 请求的各个参数
            (r"/request_everything", index.RequestEverythingHandler),
            # 文件上传
            (r"/file", index.RequestUpFileHandler),
            # 响应的相关
            (r"/write", index.WriteHandler),
            # Access to the order
            (r"/access_order", index.IndexAccessOrderHandler),
            # 加载模板的接口
            (r"/home", index.HomeHandler),
            # trans 转义
            (r"/trans", index.TransHandler),
            # 继承
            (r"/cart", index.CartHandler),

            # sql students
            (r"/teachers", index.TeachersHandler),
            # 引入其他文件
            #    StaticFileHandler
            # 用来提供静资源文件的handler
            # 作用： 可以通过tornado.web.StaticFileHandler 来映射静态文件
            # 使用：
            (r"/(.*)$", tornado.web.StaticFileHandler, {
                "path": os.path.join(config.BASE_DIR, "static/html"), "default_filename": "index.html"}),



        ]
        # 把路由给父对象调用
        # **config.settings 为配置
        super(Application, self).__init__(handlers, **config.settings)
        # 连接数据库相关
        self.db = ConnectSql(config.mysql['host'], config.mysql['user'], config.mysql['passwd'], config.mysql['dbName'],
                             config.mysql['port'])
