# coding = utf-8

import argparse
import json
from api import *
import os

commandline = argparse.ArgumentParser(description="quick use arl to working!!!")
commandline.add_argument('--del_title', dest='del_title_task', help="del all title property.")
commandline.add_argument('--del_same', dest='del_same_task', action='store_true', help='del same host.')
commandline.add_argument('--config', dest='config', help='config file')
commandline.add_argument('--generate', dest='generate_config', help='generate config file', action='store_true')


"""
登录流程： 
1. 判断命令行是否有配置文件
2. 如果命令行不指定配置文件， 则读取默认配置文件
3. 
需要信息:
url 地址,  用户名, 密码， 要执行的操作

"""

def open_config(file_path:str):
    """读取配置文件信息"""
    if not os.path.exists(file_path):
        raise Exception("该配置文件不存在!!!")
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            file_content = f.read()
        data = json.loads(file_content)
    except:
        raise Exception("配置文件读取失败!!!, 请尝试生成配置文件...")

    # print(data)
    # 检查 配置文件是否有需要的信息
    # pass

    return data


if __name__ == '__main__':
    args = commandline.parse_args()
    config = {}

    if args.generate_config:
        data = {"user_name": "test", "password": "test"}
        with open('new_conf.ini', mode='w+', encoding='utf-8') as f:
            content = json.dumps(data)
            f.write(content)
            exit(0)

    # 判断是否使用自带 config 文件
    if args.config:
        config = open_config(args.config)
    else:
        config = open_config('conf.ini')


    user = config['user_name']
    passwd = config['password']
    url = config['url']
    # print(user, passwd)


    if args.del_same_task:
        del_same_task(url, user, passwd)
    elif args.del_title_task:
        del_title_host(args.del_title_task, url, user, passwd)






