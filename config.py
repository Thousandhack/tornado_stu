import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPFILE_DIR = os.path.join(BASE_DIR, 'upfile/').replace('\\', '/')
# 参数
options = {
    "port": 8700,
    # "list": ["good", "nice", "cool"]
}

# 配置
"""
"debug": True  的效果：
自动重启
取消缓存
取消缓存静态的哈希值
提供追踪信息
"""
settings = {
    "debug": True,  # False为生产模式
    "static_path": os.path.join(BASE_DIR, "static"),  # 设置文件保存目录
    "template_path": os.path.join(BASE_DIR, "templates"),  # 设置模块文件目录
    "autoescape": None,  # 关于整个项目的自动转义关闭
}

# tornado没有自带的orm,对于数据库需要自己去适配
# python3.6+tornado 没有比较完善的驱动
# 数据库配置
mysql = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "123456",
    "dbName": "flask_demo",
    "port": 3306
}
