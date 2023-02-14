# run this script as root and usr twice


import os

hostip="192.168.31.185"

import subprocess
def runcmd(cmd):
    ret=subprocess.run(cmd.split(" "))
    if ret.returncode==0:
        print(">>> ",cmd," succ \n")
    else:
        print(">>> ",cmd," fail ",ret,"\n")

def setproxy():
    # git
    runcmd("git config --global http.proxy http://{}:23333".format(hostip))
    runcmd("git config --global https.proxy https://{}:23333".format(hostip))
    
    # docker
    def rewrite_docker_service():
        file_object = open("docker.service",'r') #创建一个文件对象，也是一个可迭代对象
        to=""
        try:
            all_the_text = file_object.read()  #结果为str类型
            to=all_the_text.replace("{target}",
                ('Environment="HTTP_PROXY=http://{}:23333"\n'+
                'Environment="HTTPS_PROXY=http://{}:23333"\n')
                .format(hostip,hostip))
            # print (type(all_the_text))
            

        finally:
            file_object.close()

        # print ("to=",to)
        with open("/usr/lib/systemd/system/docker.service",'w')as file:
            file.write(to)
        runcmd("systemctl daemon-reload")
        runcmd("systemctl restart docker.service")
    rewrite_docker_service()

setproxy();