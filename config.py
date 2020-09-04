import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPFILE_DIR = os.path.join(BASE_DIR, 'upfile/').replace('\\', '/')
# 参数
options = {
    "port": 8800,
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
}
