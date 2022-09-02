import subprocess
import sys
import os
from time import sleep
import zipfile

def run_cmd_sync(cmd):
    print("\nrun_cmd_sync begin ============================================================\n")
    subprocess.run(cmd, stderr=sys.stderr, stdout=sys.stdout)
    
    print("\nrun_cmd_sync end ============================================================\n\n")

def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir("./"+file_name + "_files"):
        pass
    else:
        os.mkdir("./"+file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,"./"+file_name + "_files/")
    
    zip_file.close()
    sleep(1)