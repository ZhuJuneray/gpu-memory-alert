FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /app

# 安装Python和pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY requirements.txt .
COPY src/ ./src/
COPY config/ ./config/
COPY main.py .

# 安装依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 运行应用
CMD ["python3", "main.py"]