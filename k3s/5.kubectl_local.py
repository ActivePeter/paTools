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





# copy /etc/rancher/k3s/k3s.yaml to ~/.kube/config
os_system_sure(f"scp root@{master_ip}:/etc/rancher/k3s/k3s.yaml k3s.yaml")
with open("k3s.yaml", 'r') as stream:
    k3s_config = stream.read()
    stream.close()
    if k3s_config.find("server: https://127.0.0.1")==-1:
        print("unsupported k3s config, please check")
        exit(1)
    k3s_config=k3s_config.replace("server: https://127.0.0.1", f"server: https://{master_ip}")
    stream = open("k3s.yaml", 'w')
    stream.write(k3s_config)
    stream.close()

# set to ~/.kube/config
os_system_sure("mkdir -p ~/.kube")
os_system_sure("cp k3s.yaml ~/.kube/config")

