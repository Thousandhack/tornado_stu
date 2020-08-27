import tornado.web


# 相当于视图
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web project")


class TestValueHandler(tornado.web.RequestHandler):
    def initialize(self, test_value_1, test_value_2):
        # 将参数传进来并初始化可以让get方法使用
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
    def get(self, *args, **kwargs):
        """
        :param request:
        :return:
        """
        if 1 == 1:
            self.send_error(status_code=500, **kwargs)
        self.write("返回的数据")
