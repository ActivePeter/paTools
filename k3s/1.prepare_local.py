import os, yaml
CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)
# chdir to the directory of this script
os.chdir(CUR_FDIR)


import os
def os_system_sure(command):
    print(f"执行命令：{command}")
    result = os.system(command)
    if result != 0:
        print(f"命令执行失败：{command}")
        exit(1)
    print(f"命令执行成功：{command}\n\n")



# docker compose up
if not os.path.exists("k3s"):
    os_system_sure('wget https://github.com/k3s-io/k3s/releases/download/v1.30.0%2Bk3s1/k3s')

if not os.path.exists("k3s-airgap-images-amd64.tar.gz"):
    os_system_sure('wget https://github.com/k3s-io/k3s/releases/download/v1.30.0%2Bk3s1/k3s-airgap-images-amd64.tar.gz')

if not os.path.exists("install.sh"):
    os_system_sure('wget https://get.k3s.io -O install.sh')

if os.path.exists("k3s"):
    print("k3s is ready")
if os.path.exists("k3s-airgap-images-amd64.tar.gz"):
    print("k3s-airgap-images-amd64.tar.gz is ready")
if os.path.exists("install.sh"):
    print("install.sh is ready")