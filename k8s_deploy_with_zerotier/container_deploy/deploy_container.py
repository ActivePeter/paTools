import subprocess
import os
import shutil
def copy_file():
    shutil.copy('文件的名字', '复制的路径位置')

def runcmd(cmd):
    ret=subprocess.run(cmd.split(" "))
    if ret.returncode==0:
        print(">>> ",cmd," succ \n")
    else:
        print(">>> ",cmd," fail ",ret,"\n")

def trydo(cb):
    try:
        cb()        
    finally:
        print("")
    
trydo(
    lambda:runcmd("tar Cxzvf /usr/local containerd-1.6.15-linux-amd64.tar.gz")
)

shutil.copy("./containerd.service","/etc/systemd/system")
runcmd("systemctl daemon-reload")
runcmd("systemctl enable --now containerd")

runcmd("install -m 755 runc.amd64 /usr/local/sbin/runc")

runcmd("mkdir -p /opt/cni/bin")
trydo(
    lambda:runcmd("tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.2.0.tgz")
)