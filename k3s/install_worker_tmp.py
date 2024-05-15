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


# # check installed k3s
# result = os.system("k3s kubectl get nodes")
# if result != 0:
#     print("k3s is not installed")
# else:
#     print("k3s is installed")
#     # # 1.reinstall
#     # print("uninstall")
#     # os_system_sure("bash /usr/local/bin/k3s-uninstall.sh")
    
#     # keep
#     exit(0)


K3S_TOKEN=
SERVER_IP=


# prepare env
os_system_sure("cp /tmp/k3s/k3s /usr/local/bin/k3s")
os_system_sure("chmod +x /usr/local/bin/k3s")
os_system_sure("mkdir -p /var/lib/rancher/k3s/agent/images/")
os_system_sure("cp /tmp/k3s/k3s-airgap-images-amd64.tar.gz /var/lib/rancher/k3s/agent/images/")


# install
os.chdir("/tmp/k3s")
os.environ['INSTALL_K3S_SKIP_DOWNLOAD']="true"
# K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken
os.environ['K3S_URL']=f"https://{SERVER_IP}:6443"
os.environ['K3S_TOKEN']=f"{K3S_TOKEN}"

os_system_sure("bash ./install.sh")

# os_system_sure("k3s kubectl get nodes")
