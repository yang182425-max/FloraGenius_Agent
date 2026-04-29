#!/bin/bash
# 自动化数据传输脚本
# 用于将本地 Windows 节点重建好的点云文件夹同步至 Linux 计算服务器
echo "开始通过 rsync 同步点云数据至 Linux 服务器..."
rsync -avz --progress ./data/ user@your_linux_server_ip:/path/to/reconstruction_workspace/
echo "同步完成！"