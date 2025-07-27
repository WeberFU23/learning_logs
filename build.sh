#!/usr/bin/env bash

# Exit on error (如果任何命令失败，脚本立即退出)
set -o errexit

# 1. 安装项目依赖
# 确保你的 requirements.txt 文件在项目根目录
pip install -r requirements.txt

# 2. 运行数据库迁移
# 如果你的 settings.py 在 learning_log 目录下，
# 且你的 Build Command 会在项目根目录执行，
# 那么你需要确保 PYTHONPATH 设置正确或者cd到正确目录
# 最常见的是直接在 build.sh 中运行：
python manage.py migrate

# 3. 收集静态文件
# --no-input 选项是为了避免 collectstatic 询问确认
python manage.py collectstatic --no-input

# 你可能还需要让脚本可执行
# chmod +x build.sh (在你本地Git提交前执行)
