
import sys
import time
from selenium import webdriver
import yaml
import os

CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)

# chdir to the directory of this script
os.chdir(CUR_FDIR)


def flush_print(content):
    print(content)
    sys.stdout.flush()

def entry_point():
    flush_print("Auto login task started\n")

    config_data={}
    with open("config.yml", 'r') as stream:
        config_data = yaml.safe_load(stream)
    
    userid=config_data['id']
    userpw=config_data['pw']
    # flush_print(f"{userid}, {userpw}")



    option=webdriver.ChromeOptions()

    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')

    flush_print("Chrome loaded\n")
    

    loop_cnt=0
    while True:
        flush_print(f"loop {loop_cnt}")
        try:
            flush_print("a")
            driver=webdriver.Chrome(options=option)
            flush_print("b")
            driver.get("http://baidu.com")
            flush_print("c")
            # 键入账号，需要修改成自己的账号密码
            driver.find_element_by_id("userphone").send_keys(userid)
            driver.find_element_by_id("password").send_keys(userpw)
            driver.find_element_by_id("mobilelogin_submit").click()

        except Exception as error:
            print("An error occurred:", error)

        time.sleep(30)

entry_point()