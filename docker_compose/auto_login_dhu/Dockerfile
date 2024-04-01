# 使用官方的 Python 3 镜像作为基础镜像
FROM ubuntu:20.04

# 切换到 root 用户
USER root

# RUN echo "\
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse\n\
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse\n\
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse\n\
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse\n\
# " > /etc/apt/sources.list

# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E88979FB9B30ACF2
RUN apt-get update

RUN apt-get install -y \
    python3 \
    python3-pip 

RUN apt-get install -y fonts-liberation
RUN apt-get install -y libasound2

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y libatk-bridge2.0-0
RUN apt-get install -y libatk1.0-0
RUN apt-get install -y libatspi2.0-0
RUN apt-get install -y libcairo2
RUN apt-get install -y libcups2
RUN apt-get install -y libcurl4
RUN apt-get install -y libdbus-1-3
RUN apt-get install -y libdrm2
RUN apt-get install -y libgbm1
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libgtk-3-0
RUN apt-get install -y libnspr4
RUN apt-get install -y libnss3
RUN apt-get install -y libpango-1.0-0
RUN apt-get install -y libwayland-client0
RUN apt-get install -y libx11-6
RUN apt-get install -y libxcb1
RUN apt-get install -y libxcomposite1
RUN apt-get install -y libxdamage1
RUN apt-get install -y libxext6
RUN apt-get install -y libxfixes3
RUN apt-get install -y libxkbcommon0
RUN apt-get install -y libxrandr2
RUN apt-get install -y wget
RUN apt-get install -y xdg-utils

# 安装 Selenium
RUN pip3 install selenium==3.141.0
RUN pip3 install --upgrade urllib3==1.22
RUN pip3 install pyyaml

# chrome & chrome driver
COPY google-chrome-stable_current_amd64.deb /auto_login/chrome.deb
RUN dpkg -i /auto_login/chrome.deb

COPY chromedriver /usr/bin/chromedriver
RUN chmod 775 /usr/bin/chromedriver

COPY login_task.py /auto_login/script.py
COPY entrypoint.sh /auto_login/entrypoint.sh

CMD ["bash", "/auto_login/entrypoint.sh"]
