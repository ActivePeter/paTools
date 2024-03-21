FROM python:3.9

# 安装 Chrome 浏览器和对应版本的驱动程序
RUN apt-get update && apt-get install -y \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get -qqy install google-chrome-stable \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge --auto-remove -y curl \
    && rm -rf /src/*.deb

# 安装 Selenium
RUN pip install selenium

# 在这里添加其他依赖库的安装步骤，如果有的话

# 将脚本文件复制到 Docker 容器中
COPY login_task.py /path/to/your/script.py

# 设置 Docker 容器启动时执行的命令
CMD ["python", "/path/to/your/script.py"]
