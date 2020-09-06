import tornado.web
import config
import json
import os


# 相当于视图
class IndexReturnHandler(tornado.web.RequestHandler):
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
    def get(self, demo_01, demo_02, *args, **kwargs):
        """
        利用HTTP协议向服务器传递参数
            提取uri 的特定部分
            get方法传递参数
            post方式传递参数
        request 对象
        tornado.web.RequestHandler对象
            可以获取get请求，也可以获取post请求
            在http报文的报头的自定义
        tornado.httputiil.HTTPFile对象

        访问：http://127.0.0.1:8800/request_value/one/two
        打印one two

        加了：?P<demo_01> 在handler 不需要排序
        访问就打印： two one

        访问：http://127.0.0.1:8800/request_value/one/two?a=1&b=2
        打印：a的值为: 1
              two one

        访问：http://127.0.0.1:8800/request_value/one/two?c=1&c=2
        # 使用：c = self.get_query_arguments("c")
        # 打印：
        # ['1', '2']
        :param args:
        :param kwargs:
        :return:
        """
        # self.get_query_argument(name,default=ARG_DEFAULT,strip=True)
        # name如果出现多个同名参数会返回最后一个值
        # 如果设置了未传的name的参数，返回defaul里面的默认值
        # 如果没有设置default值,那么会抛出tornado.web.MissingArgumentError异常
        # strip=True 表示去掉前后空格
        a = self.get_query_argument("a", default=None, strip=True)
        print("a的值为:", a)
        print(demo_01, demo_02)
        c = self.get_query_arguments("c", strip=True)
        print(c)
        self.write("get request value success")

    def post(self, *args, **kwargs):
        """
        访问url: http://127.0.0.1:8800/request_value/one/two
        使用form-data的方式加name  和对应的值
        返回打印结果：hsz
        :param args:
        :param kwargs:
        :return:
        """
        name = self.get_body_argument('name', default=None, strip=True)  #
        print(name)
        # self.get_query_arguments("name")
        self.write("post request value success")


class RequestPostVlaueHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        """
        访问url: http://127.0.0.1:8800/request_value
        使用json数据传参：
                {
                    "name":"18611111111",
                    "password":"123456"
                }
        最后得到打印：
            {'name': '18611111111', 'password': '123456'}
            18611111111
        :param args:
        :param kwargs:
        :return:
        """
        post_body = self.request.body
        # 反序列化body数据
        body_data = json.loads(post_body.decode('utf8'))
        print(body_data)
        name = body_data.get('name')
        print(name)
        self.write("post request value success")


class RequestEverythingHandler(tornado.web.RequestHandler):
    def post(self):
        """
        Request对象
            method HTTP请求的方式
            Host 被请求的主机名
            Uri  请求的完整资源地址，包括路径和get查询参数部分
            Path 请求的路径部分
            Query 请求的参数部分
            Version 使用的HTTP版本
            Headers 请求头
            Body   请求体数据
            Remote_ip 客户端的ip
            Files 用户上传的文件，字典类型

        HTTP 1.1 特点长连接

        例子：http://127.0.0.1:8800/request_everything?a=1
            {
                "name":"hsz"
            }

        对应打印结果为：
            post_mthod = POST
            post_uri= /request_everything?a=1
            post_host= 127.0.0.1:8800
            post_query= a=1
            post_version= HTTP/1.1
            post_headers= Con: haha
            Content-Type: application/json
            User-Agent: PostmanRuntime/7.26.3
            Accept: */*
            Cache-Control: no-cache
            Postman-Token: 6cc555af-ab09-403a-840c-52f62ebbd7d1
            Host: 127.0.0.1:8800
            Accept-Encoding: gzip, deflate, br
            Connection: keep-alive
            Content-Length: 22

            post_body= b'{\r\n    "name":"hsz"\r\n}'
            post_remote_ip= 127.0.0.1
            post_files= {}
        :return:
        """
        post_mthod = self.request.method
        print("post_mthod =", post_mthod)
        post_uri = self.request.uri
        print("post_uri=", post_uri)
        post_host = self.request.host
        print("post_host=", post_host)
        post_query = self.request.query
        print("post_query=", post_query)
        post_version = self.request.version
        print("post_version=", post_version)

        post_headlers = self.request.headers
        print("post_headers=", post_headlers)

        post_body = self.request.body
        print("post_body=", post_body)

        post_remote_ip = self.request.remote_ip
        print("post_remote_ip=", post_remote_ip)

        post_files = self.request.files
        print("post_files=", post_files)
        self.write("request everything ")


class RequestUpFileHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        """
        tornado.httputil.HTTPFile 对象
        作用： 接收到的文件对象
        属性：
            1.filename 文件的实际名字
            2.body  文件的数据实体
            3.content_type 文件的类型
        发送一个demo.txt 的文件：
        打印的内容为：
        {'the_file': [{'filename': 'demo.txt', 'body': b'the test content!!!', 'content_type': 'text/plain'}]}
        多个文件：
        {
            'the_file':
            [{
                'filename': 'demo.txt',
                'body': b'the test content!!!',
                'content_type': 'text/plain'
            }],
            'two':
            [{
                'filename': 'demo.txt',
                'body': b'the test content!!!',
                'content_type': 'text/plain'
            }]
        }
        :param args:
        :param kwargs:
        :return:
        """
        files = self.request.files
        # 以下实现多文件上传（暂时,优化成图片名字一样的情况也可以，也就是连续上传两次一样的图片目前会有问题）
        for inputname in files:
            file_list = files[inputname]
            for file_obj in file_list:
                # 存储路径
                file_path = os.path.join(config.UPFILE_DIR + file_obj.filename)
                with open(file_path, "wb") as f:
                    f.write(file_obj.body)
        self.write("upload file success !!!")


class WriteHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        self.write 可以多次，但是self.finsh后self.write就会失效
        write 返回json数据
        :param args:
        :param kwargs:
        :return:
        """
        self.write("write success one")
        self.write("write success two")
        # 刷新缓冲区，关闭当次请求通道
        self.finish()


class IndexAccessOrderHandler(tornado.web.RequestHandler):
    """
    正常执行顺序：
    http://127.0.0.1:8800/access_order
    set_default_headers
    initialize
    prepare
    get   HTTP方法
    on_finish

    异常运行：上面的URL
   self.send_error(500)  # 触发write_error方法
   内置方法运行顺序：
    set_default_headers
    initazlize
    prepare
    HTTP方法
    set_default_headers
    write_error
    ERROR:tornado.access:500 GET /access_order (127.0.0.1) 1.00ms
    on_finish

    """

    def initialize(self):
        print("initazlize")

    def prepare(self):
        print("prepare")

    def get(self, *args, **kwargs):
        print("HTTP方法")
        self.send_error(500)  # 触发write_error方法
        self.write("sunck is a good man")

    def set_default_headers(self):
        print("set_default_headers")

    def write_error(self, status_code: int, **kwargs):
        """
        出错的情况下才会触发
        :param status_code:
        :param kwargs:
        :return:
        """
        print("write_error")

    def on_finish(self) -> None:
        print("on_finish")


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        返回home的相应网页
        :param args:
        :param kwargs:
        :return:
        """
        tmp = 100
        per = {
            "name": "hsz",
            "age": 25
        }
        self.render('home.html', num=tmp, per=per)


class TransHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        默认的话就是自动转义，就是过去后仅仅是字符串
        :param args:
        :param kwargs:
        :return:
        """
        str = "<h1>hsz is a good man<h1/>"
        self.render("trans.html", str=str)


class CartHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cart.html', title="cart")


