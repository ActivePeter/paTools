# 使用基础镜像
FROM alpine:latest

# 复制配置文件
COPY frpc /usr/local/bin
RUN chmod +x /usr/local/bin/frpc

# 运行 frpc
CMD ["frpc", "-c", "/etc/frp/frpc.ini"]