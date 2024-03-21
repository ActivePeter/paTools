# 使用一个基础的 Ubuntu 镜像作为基础
FROM ubuntu:latest

# 安装所需的软件包
RUN apt-get update && \
    apt-get install -y \
    ssh \
    net-tools \
    vim \
    sudo \
    git

# 设置默认的 shell 环境为 bash
ENV SHELL=/bin/bash

# 启用 root 账户的 SSH 登录
RUN sed -ri 's/^#PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config

# 启动 SSH 服务
RUN service ssh start

RUN echo 'root:11111' | chpasswd

# 对外暴露 SSH 端口
EXPOSE 22

# 设置默认工作目录
WORKDIR /root

# 执行 bash，保持容器运行
CMD ["tail", "-f", "/dev/null"]
