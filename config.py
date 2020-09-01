import os

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
    "static_path": "",  # 设置文件保存目录
    "template_path": "",  # 设置模块文件目录
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPFILE_DIR = os.path.join(BASE_DIR, 'upfile/').replace('\\', '/')
