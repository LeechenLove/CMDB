import sys
import os


BASE_DIR = os.path.dirname(os.getcwd())
print(BASE_DIR)
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

a = sys.argv
print(a)
print(type(a))

