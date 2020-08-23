import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# define 用来定义变量的
"""
tornado.options.define(
        name: str,   # 选项变量名，必须保证其唯一性
        default: Any = None, # 设置选项变量的默认值，默认为None
        type: type = None, # 设置变量的类型,从命令行或配置文件导入tornado会根据类型转换输入的值，转换不成会保错
       # 如果没有设置type值，会根据default的值进行转换
       # 如果没有设置type值且没有default的值，那么不进行转换
        help: str = None,  # 选项变量的帮助提示信息
        metavar: str = None,
        multiple: bool = False,  # 设置选项变量是否可以为多个值，
        group: str = None,
        callback: Callable[[Any], None] = None,
)
"""

tornado.options.define("port", default=8000, type=int)
tornado.options.define("list", default=[], type=str)

"""
tornado.options.options
全家的options对象，所有定义的选项变量都会作为该对象的属性
"""

"""
获取参数的方法： tornado.options.parse_command_line()  转换命理行参数
"""


class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web four!!!")


if __name__ == "__main__":
    # 转换命令行参数，并保存到tornado.options.options
    tornado.options.parse_command_line()
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
    # 运行以下命令开启
    # >python server_04.py --port=8800 --list=good,nice,cool
    # 能这样，但是以后不会这样运行项目

    # 从配置文件导入参数
    # tornado.options.parse_config_file(path)

    # 关闭日志的情况下的命令：
    # >python server_04.py --port=8800 --list=good,nice,cool --logging=None
