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
        self.write(per)  # 也可以不需要转  推荐使用
        # import json
        # # 将字典转化为json
        # self.write(json.dumps(per))
