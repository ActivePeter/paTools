#!/bin/bash

# 目标备份目录
backup_dir="/pvcdata/backup"

# 排除的目录列表
exclude_dirs=(
    "/proc"
    "/sys"
    "/dev"
    "/mnt"
    "/tmp"
)

# 构建排除参数
exclude_params=""
for dir in "${exclude_dirs[@]}"; do
    exclude_params+=" --exclude=$dir"
done

# 执行备份
sudo rsync -av --delete $exclude_params / $backup_dir

# 验证备份是否成功
if [ $? -eq 0 ]; then
    echo "备份成功"
else
    echo "备份失败，请检查错误信息"
fi
