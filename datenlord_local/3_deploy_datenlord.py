import yaml
f = open("./valuemap.yaml")
y = yaml.load(f)
file_object = open("3_deploy_datenlord.sh",'r') #创建一个文件对象，也是一个可迭代对象

import subprocess
def runcmd(cmd):
    ret=subprocess.run(cmd.split(" "))
    if ret.returncode==0:
        print(">>> ",cmd," succ \n")
    else:
        print(">>> ",cmd," fail ",ret,"\n")

try:
    all_the_text = file_object.read()  #结果为str类型
    for key in y:
        # print("kv",key,y[key])
        all_the_text=all_the_text.replace("$"+key,str(y[key]))
        all_the_text=all_the_text.replace("${"+key+"}",str(y[key]))
    print ("all_the_text=",all_the_text)
    temp = 'temp.sh'
    with open(temp, 'w') as file_object:
        file_object.write(all_the_text)
    runcmd("chmod 777 temp.sh")
    runcmd("sh ./temp.sh")
    runcmd("rm -r temp.sh")
finally:
    file_object.close()