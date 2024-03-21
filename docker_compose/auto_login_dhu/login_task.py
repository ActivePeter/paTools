mport time

from selenium import webdriver



option=webdriver.ChromeOptions()

option.add_argument('--headless')

option.add_argument('--no-sandbox')#fix:DevToolsA

option.add_argument('--disable-gpu')

#fix:DevTools

option.add_argument('--disable-dev-shm-usage')



import subprocess



def disable_network_interface(interface_name):

   try:

       subprocess.run(['sudo', 'ifconfig', interface_name, 'down'], check=True)

       print(f"Successfully disabled {interface_name}.")



   except subprocess.CalledProcessError as e:

       print(f"Error disabling {interface_name}: {e}")



def enable_network_interface(interface_name):

   try:

       subprocess.run(['sudo', 'ifconfig', interface_name, 'up'], check=True)

       print(f"Successfully enabled {interface_name}.")



   except subprocess.CalledProcessError as e:

       print(f"Error enabling {interface_name}: {e}")



# Example usage

interface_name = 'eth0' # Replace with your actual network interface name





import socket



def check_network_connection(host="www.baidu.com", port=80, timeout=5):

   try:

       socket.create_connection((host, port), timeout=timeout)

       print("Network connection is active.")

       return True

   except socket.error as ex:

       print(f"Network connection failed: {ex}")

       return False







while True:

   if not check_network_connection():

       disable_network_interface(interface_name)

       # Do some work while the network interface is disabled

       enable_network_interface(interface_name)

   # sleep 1min

   try:

       #option.add_argument('--remote-debugging-port=9222

       driver=webdriver.Chrome(chrome_options=option)

       driver.get("http://1.2.3.4")



       # 键入账号，需要修改成自己的账号密码

       driver.find_element_by_id("userphone").send_keys("")

       driver.find_element_by_id("password").send_keys("")

       driver.find_element_by_id("mobilelogin_submit").click()



   except:

       print("err")





   time.sleep(30)