# -*- coding:utf-8 -*-

import json
import time
import requests

from core import info_collection
from conf import settings


class ArgvHandler(object):

    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        """
        分析参数，如果有参数指定的方法，则执行该功能，如果没有，打印帮助说明。
        :return:
        """
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.help_msg()

    @staticmethod
    def help_msg():
        """
        帮助说明
        :return:
        """
        msg = '''
        参数名               功能

        collect_data        测试收集硬件信息的功能

        report_data         收集硬件信息并汇报
        '''
        print(msg)

    @staticmethod
    def collect_data():
        """收集硬件信息，用于测试！"""
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        """
        收集硬件信息，然后发送到服务器。
        :return:
        """
        # 收集信息
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        # 将数据打包到一个字典内，并转换为json格式
        data = json.dumps({"asset_data": asset_data})
        # 根据settings中的配置，构造url
        url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
        print('正在将数据发送至： [%s]  ......' % url)
        try:
            headers = {'content-type': 'application/json'}
            response = requests.post(url=url, data=data, headers=headers)
            message = response.text
        except Exception as e:
            message = "发送失败" + f"  错误原因：{e}"
            print(f"发送失败，错误原因：{e}")

        # 记录发送日志
        with open(settings.PATH, 'ab') as f:
            log = f"发送时间：{time.strftime('%Y-%m-%d %H:%M:%S')} \t 服务器地址：{url} \t 返回结果：{message} \n"
            f.write(log.encode())
            print("日志记录成功！")
