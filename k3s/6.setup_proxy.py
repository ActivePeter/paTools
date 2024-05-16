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
    # if 'is_master' in conf:
    #     continue

    ip=conf['ip']

    PROXY="http://192.168.31.53:7890"
    export=f"""
HTTP_PROXY={PROXY}
HTTPS_PROXY={PROXY}
NO_PROXY=127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
"""
    # prepare remote
    if 'is_master' in conf:
        os_system_sure(f"ssh root@{ip} 'echo \"{export}\" >> /etc/systemd/system/k3s.service.env'")
        os_system_sure(f"ssh root@{ip} 'systemctl daemon-reload'")
        os_system_sure(f"ssh root@{ip} 'systemctl restart k3s'")
    else:
        os_system_sure(f"ssh root@{ip} 'echo \"{export}\" >> /etc/systemd/system/k3s-agent.service.env'")
        os_system_sure(f"ssh root@{ip} 'systemctl daemon-reload'")
        os_system_sure(f"ssh root@{ip} 'systemctl restart k3s-agent'")

    
    # break

