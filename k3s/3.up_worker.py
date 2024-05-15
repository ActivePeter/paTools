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


with open("config.yml", 'r') as stream:
    config_data = yaml.safe_load(stream)

if not isinstance(config_data, dict):
    print("config.yml is not a dictionary")
    exit(1)


master_node=None
master_node_ip=None

for node, conf in config_data.items():
    if not isinstance(conf, dict):
        print(f"config.yml[{node}] is not a dictionary")
        exit(1)
    
    if 'ip' not in conf:
        print(f"config.yml[{node}]['ip'] is not found")
        exit(1)

    if 'is_master' in conf:
        master_node=node
        master_ip=conf['ip']

if master_node==None:
    print("master node is not found")
    exit(1)

os_system_sure("mkdir -p uplog")

def rcmd(ip,cmd):
    return f"ssh root@{ip} '{cmd}'"

# get master token
import subprocess
process = subprocess.Popen(rcmd(master_ip,'cat /var/lib/rancher/k3s/server/token'),stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()
if process.returncode == 0:
    K3S_TOKEN=output.decode('utf-8').strip()
    print(f"K3S_TOKEN: {K3S_TOKEN}")
else:
    print("server is not ready")
    exit(1)


# replace content in install_worker.py
with open("install_worker_tmp.py", 'r') as stream:
    install_worker_content = stream.read()
    # print(install_worker_content)
    install_worker_content=install_worker_content \
        .replace("K3S_TOKEN=",f"K3S_TOKEN='{K3S_TOKEN}'") \
        .replace("SERVER_IP=",f"SERVER_IP='{master_ip}'")
    # print(install_worker_content)
    with open("install_worker.py", 'w') as stream:
        stream.write(install_worker_content)
        stream.close()





for node, conf in config_data.items():
    if 'is_master' in conf:
        continue

    ip=conf['ip']
    # prepare remote
    os_system_sure(f"ssh root@{ip} 'mkdir -p /tmp/k3s'")
    os_system_sure(f"scp k3s root@{ip}:/tmp/k3s/k3s")
    os_system_sure(f"scp k3s-airgap-images-amd64.tar.gz root@{ip}:/tmp/k3s/k3s-airgap-images-amd64.tar.gz")
    os_system_sure(f"scp install.sh root@{ip}:/tmp/k3s/install.sh")
    os_system_sure(f"scp install_worker.py root@{ip}:/tmp/k3s/install_worker.py")
    os_system_sure(f"ssh root@{ip} 'ls /tmp/k3s/'")


    # remote run
    os_system_sure(f"ssh root@{ip} 'python3 /tmp/k3s/install_worker.py'")
    # break

