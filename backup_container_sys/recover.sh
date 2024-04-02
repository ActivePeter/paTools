#!/bin/bash

# 源备份目录
backup_dir="/pvcdata/backup"

# 目标恢复目录
restore_dir="/"

# 执行恢复
sudo rsync -av $backup_dir/ $restore_dir

# 验证恢复是否成功
if [ $? -eq 0 ]; then
    echo "恢复成功"
else
    echo "恢复失败，请检查错误信息"
fi
