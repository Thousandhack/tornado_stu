import tornado.web


# 相当于视图
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的方法
    def get(self):
        #  给浏览器响应信息
        self.write("hello tornado web project")
