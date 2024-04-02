import os
import yaml

CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)
# chdir to the directory of this script
os.chdir(CUR_FDIR)


# 打开并读取YAML文件
with open('proxy.yaml', 'r') as file:
    # 加载YAML数据
    data = yaml.safe_load(file)
HOST=data['host']
PORT=data['port']


# docker compose up
os.system('git config --global http.proxy http://'+HOST+':'+PORT)
os.system('git config --global https.proxy http://'+HOST+':'+PORT)
# os.system('ex')