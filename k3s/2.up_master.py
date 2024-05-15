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


# prepare remote
os_system_sure(f"ssh root@{master_ip} 'mkdir -p /tmp/k3s'")
os_system_sure(f"scp k3s root@{master_ip}:/tmp/k3s/k3s")
os_system_sure(f"scp k3s-airgap-images-amd64.tar.gz root@{master_ip}:/tmp/k3s/k3s-airgap-images-amd64.tar.gz")
os_system_sure(f"scp install.sh root@{master_ip}:/tmp/k3s/install.sh")
os_system_sure(f"scp install_server.py root@{master_ip}:/tmp/k3s/install_server.py")
os_system_sure(f"ssh root@{master_ip} 'ls /tmp/k3s/'")


# remote run
os_system_sure(f"ssh root@{master_ip} 'python3 /tmp/k3s/install_server.py'")

# for node, conf in config_data.items():
#     if 'is_master' in conf:
#         continue
#     os_system_sure(f"k3sup join --ip {conf['ip']} --server-ip {master_ip} --user root &> uplog/node_{node}.log")

