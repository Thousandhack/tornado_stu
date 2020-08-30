import tornado.web


# 相当于视图
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web project")
        # 主要作用为刷新缓冲区，关闭当次请求通道
        # 在finish下边就不要在write
        # self.finish()


class TestValueHandler(tornado.web.RequestHandler):
    def initialize(self, test_value_1, test_value_2):
        """
        # 将参数传进来并初始化可以让get方法使用
        接收参数
        :param test_value_1:
        :param test_value_2:
        :return:
        """
        self.test_value_1 = test_value_1
        self.test_value_2 = test_value_2

    # 处理get请求的方法
    def get(self, *args, **kwargs):
        print(self.test_value_1)
        print(self.test_value_2)
        self.write("Test Value tornado web project")


class JsonHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        per = {
            "name": "hsz",
            "age": 18,
            "heigth": 175
        }
        # 自定义请求头
        self.set_header("Content-Type", "application/json;charset=UTF-8")
        self.set_header("suck", "good")
        self.write(per)  # 也可以不需要转  推荐使用
        # import json
        # # 将字典转化为json
        # self.write(json.dumps(per))

        #  设置请求头的作用
        # self.set_header() 设置请求头的作用


class HeaderHandler(tornado.web.RequestHandler):

    def set_default_headers(self) -> None:
        """
        # http相应方法之前被调用，可以重写该方法，来预先设置headers
        一般这样用
        :return:
        """
        self.set_header("Content-Type", "test/html;charset=UTF-8")

    def get(self, *args, **kwargs):
        """
        如果这边还使用self.set_header那就会使用self.set_header
        :param args:
        :param kwargs:
        :return:
        """
        self.set_status(status_code=200, reason=None)
        self.write("返回的数据")


class StatusCodeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        self.set_status(status_code=200,reason=None)
        status_code 状态码，为int类型
        reason 为返回的消息，最后为英文


        :param request:
        :return:
        """
        self.set_status(status_code=400, reason="request bad")
        self.write("返回的数据")


class RedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        :param request:
        :return:
        """
        self.redirect("https://www.huya.com/")
        # self.write("返回的数据")


class ErrorHandler(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.write("服务器内部错误")
        elif status_code == 400:
            self.write("请求参数错误")
        else:
            self.write("不知道发生什么错误")

    def get(self, *args, **kwargs):
        # """
        # 抛出HTTP的错误状态码，抛出错误后tornado会调用write_error()方法进行处理，并
        # 注意：在send_error之下就不要响应输出了
        #
        # 用来处理send_error抛出的错误信息，并返回给浏览器错误界面
        # :param args:
        # :param kwargs:
        # :return:
        # """
        flag = self.get_query_argument('flag')  # 接收网址上的参数
        print(flag, type(flag))
        # flag = '1'
        if flag == '1':
            self.send_error(status_code=500)
            # 紧接的运行的write_error方法，里面有相应的返回消息
        self.write("right!")


# """
#         访问：http://127.0.0.1:8800/is_error?flag=1
#         Traceback (most recent call last):
#           File "C:\Users\admin\Envs\tornado_demo\lib\site-packages\tornado\web.py", line 1590, in _execute
#             result = method(*self.path_args, **self.path_kwargs)
#           File "E:\tornado\tornado_stu\views\index.py", line 91, in get
#             self.write("right!")
#           File "C:\Users\admin\Envs\tornado_demo\lib\site-packages\tornado\web.py", line 738, in write
#             raise RuntimeError("Cannot write() after finish()")
#         RuntimeError: Cannot write() after finish()
# """

class RenameHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("rename 111111")


class OneHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        通过self.reverse_url("rename_demo")获取接口的真正的名称
        rename_demo 为路由中name的值，然后最后可以发到访问真正url的接口
        这边的例子，即：RenameHandler
        :param args:
        :param kwargs:
        :return:
        """
        url = self.reverse_url("rename_demo")
        self.write("<a href='%s'>去rename一个页面，one,one</a>" % (url))


class RequestVlaueHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        利用HTTP协议向服务器传递参数
            提取uri 的特定部分
            get方法传递参数
            post方式传递参数
        request 对象
        tornado.web.RequestHandler对象
        :param args:
        :param kwargs:
        :return:
        """
        pass
