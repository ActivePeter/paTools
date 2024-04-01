import os
import re
import subprocess

CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)
CUR_F=os.path.basename(__file__)

# chdir to the directory of this script
os.chdir(CUR_FDIR)

# download the chromedriver and google-chrome install package manully
# https://drive.google.com/drive/folders/1qntkTzQkG70V_5Yvi7Zu3SapXMZf_k_8?usp=sharing

os.system(f'docker tag auto_login_dhu hanbaoaaa/auto_login_dhu:latest')
os.system(f'docker push hanbaoaaa/auto_login_dhu:latest')