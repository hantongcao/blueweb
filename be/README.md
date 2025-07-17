# Bluenote-Be 项目 README

## 项目介绍
欢迎来到 Bluenote-Be 项目！本项目旨在提供一个高性能的后端服务，基于 FastAPI 框架构建。

## 前提条件
- Python 3.11 或更高版本
- [uv](https://docs.astral.sh/uv/) - 现代Python包管理器
- Git

## 安装 uv
如果您还没有安装 uv，请运行以下命令：

```bash
# macOS 和 Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **注意**: 本项目已配置国内镜像源（清华大学、阿里云、豆瓣），可以显著提升包下载速度。

## 克隆项目
首先，克隆本项目到本地：

```bash
git clone https://jihulab.com/mahuatong/bluenote-be.git
cd bluenote-be/
```

## 快速开始

### 1. 安装依赖
使用 uv 安装项目依赖：

```bash
uv sync
```

### 2. 启动服务
启动开发服务器：

```bash
# 方式1: 直接使用 uv 运行
uv run python main.py

# 方式2: 使用 Makefile
make run

# 方式3: 使用启动脚本
python run.py
```

服务启动后，您可以通过 `http://localhost:8000` 访问 API。

## 常用命令

### 使用 Makefile（推荐）
```bash
# 查看所有可用命令
make help

# 安装依赖
make install

# 运行应用
make run

# 添加新依赖
make add PACKAGE=package_name

# 数据库迁移
make migrate

# 创建新迁移
make migration MESSAGE="migration description"
```

### 直接使用 uv 命令
```bash
# 安装依赖（使用国内镜像源和系统Python）
uv sync --python python3 --index-url https://mirrors.aliyun.com/pypi/simple/

# 添加新依赖
uv add package_name --python python3 --index-url https://mirrors.aliyun.com/pypi/simple/

# 添加开发依赖
uv add --dev package_name --python python3 --index-url https://mirrors.aliyun.com/pypi/simple/

# 移除依赖
uv remove package_name

# 更新依赖
uv lock --upgrade --python python3 --index-url https://mirrors.aliyun.com/pypi/simple/

# 查看依赖树
uv tree

# 运行应用
uv run python main.py
```

## 注意事项
如果在克隆仓库时遇到网络问题，请确保网络连接稳定或尝试更换网络环境。如果问题仍然存在，请检查链接的合法性。

## 贡献
如果您想为本项目贡献代码，请在提交前确保您的代码风格与项目保持一致，并通过所有测试。

感谢您使用 Bluenote-Be！
