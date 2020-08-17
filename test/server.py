import tornado.web
import tornado.ioloop


# 类比django的视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado web!!!")


if __name__ == "__main__":
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    app.listen(8800)
    # http://127.0.0.1:8800/
    # 返回：hello tornado web!!!
    tornado.ioloop.IOLoop.current().start()
