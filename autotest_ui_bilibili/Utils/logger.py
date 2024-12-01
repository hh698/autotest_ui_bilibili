import logging
from logging.handlers import RotatingFileHandler
import time
# from Common.file_config import FileConfig
from Utils.file_config import FileConfig

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
handler_2 = RotatingFileHandler(FileConfig().get_path(type="running_logs") + "/Web_Autotest_{0}.log".format(curTime),
                                backupCount=20, encoding='utf-8')
print(handler_2)
# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

"""
flowchart TD
    A[开始] --> B[导入模块]
    B --> C[设置日志格式]
    C --> D[创建控制台处理器]
    D --> E[获取当前时间]
    E --> F[创建文件处理器]
    F --> G[配置日志]
    G --> H[结束]
    
导入模块：导入必要的模块和类。
设置日志格式：定义日志的输出格式和日期格式。
创建控制台处理器：创建一个 StreamHandler 将日志输出到控制台。
获取当前时间：使用 time.strftime 获取当前时间，用于日志文件命名。
创建文件处理器：创建一个 RotatingFileHandler 将日志输出到文件，并设置日志文件的存储路径和轮转策略。
配置日志：使用 logging.basicConfig 配置日志的基本设置，包括格式、日期格式、日志级别和处理器。
结束：完成日志配置。
"""