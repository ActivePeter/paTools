# service_name: auto_login_dhu
# entry_python_abs_path: /home/pa/桌面/auto_login/login_loop.py


import yaml
import os
import sys

CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)
# chdir to the directory of this script
os.chdir(CUR_FDIR)


def os_system_sure(command):
    print(f"执行命令：{command}")
    result = os.system(command)
    if result != 0:
        print(f"命令执行失败：{command}")
        exit(1)
    print(f"命令执行成功：{command}\n\n")



# Load service information from YAML file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

service_name = config['service_name']
entry_python_abs_path = config['entry_python_abs_path']


# system service
SERVICE=f"""[Unit]
Description={service_name}
After=network.target

[Service]
Type=simple
ExecStart={sys.executable} {entry_python_abs_path}
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
"""


# Write the service content to a systemd service file
service_file_path = f"/etc/systemd/system/{service_name}.service"
with open(service_file_path, "w") as service_file:
    service_file.write(SERVICE)

# Reload systemd to recognize the new service
os_system_sure("systemctl daemon-reload")

# Enable the service to start on boot
os_system_sure(f"systemctl enable {service_name}")

# Start the service immediately
os_system_sure(f"systemctl start {service_name}")

print(f"服务 {service_name} 已成功创建并启动。")