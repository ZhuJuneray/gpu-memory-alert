# GPU Memory Alert

一个用于监控GPU内存使用率并通过Telegram发送告警的工具。当GPU内存使用率低于设定阈值时，系统会通过Telegram机器人发送通知。

## 功能特点

- 实时监控所有可用GPU的内存使用率
- 可配置的内存使用率阈值
- 通过Telegram机器人发送告警消息
- 可设置告警冷却时间，避免过于频繁的通知
- 支持Docker部署

## 系统要求

- Python 3.8+
- NVIDIA GPU
- NVIDIA驱动程序
- Docker（可选，用于容器化部署）

## 配置说明

在开始使用之前，需要配置 `config/config.yaml` 文件：

```yaml
telegram:
  bot_token: "YOUR_BOT_TOKEN"  # Telegram机器人的API Token
  chat_id: "YOUR_CHAT_ID"      # 接收告警消息的Chat ID

monitor:
  threshold: 20                # GPU内存使用率阈值（百分比）
  check_interval: 60           # 检查间隔（秒）
  cooldown: 300               # 两次告警之间的最小间隔（秒）
```

## 安装步骤

### 方法1：直接运行

1. 克隆仓库：
```bash
git clone https://github.com/your-username/gpu-memory-alert.git
cd gpu-memory-alert
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置设置：
   - 复制配置模板：`cp config/config.yaml.example config/config.yaml`
   - 编辑 `config/config.yaml`，填入您的 Telegram Bot Token 和 Chat ID

4. 运行程序：
```bash
python main.py
```

### 方法2：Docker部署

1. 构建Docker镜像：
```bash
docker build -t gpu-memory-alert .
```

2. 运行容器：
```bash
docker run --gpus all \
  -v $(pwd)/config:/app/config \
  gpu-memory-alert
```

## 获取 Telegram Bot Token 和 Chat ID

### 获取 Bot Token
1. 在 Telegram 中找到 @BotFather
2. 发送 /newbot 命令
3. 按照提示设置机器人名称
4. 获得 Bot Token

### 获取 Chat ID
1. 发送消息给 @userinfobot
2. 机器人会返回您的 Chat ID

## 告警消息示例

当GPU内存使用率低于阈值时，您将收到类似这样的消息：

```
🚨 Low GPU Memory Alert:

GPU 0: 15.23% memory usage
GPU 1: 18.45% memory usage
```

## 故障排除

1. 确保已安装NVIDIA驱动并且可以使用 `nvidia-smi` 命令
2. 检查 Telegram Bot Token 是否正确
3. 确认 Chat ID 格式正确
4. 检查系统防火墙是否允许程序访问 Telegram API

## 常见问题

Q: 程序无法检测到GPU？
A: 确保已正确安装NVIDIA驱动，并且可以通过 `nvidia-smi` 命令查看GPU状态。

Q: 没有收到Telegram消息？
A: 检查网络连接，确保可以访问Telegram API，并验证Bot Token和Chat ID是否正确。

## 日志

程序运行日志将显示在控制台中，包含以下信息：
- 系统启动状态
- GPU检测结果
- 告警发送状态
- 错误信息（如果有）

## 贡献指南

欢迎提交 Pull Request 或创建 Issue 来帮助改进这个项目。

## 许可证

本项目采用 MIT 许可证。