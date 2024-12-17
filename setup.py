from setuptools import setup, find_packages

setup(
    name="gpu-memory-alert",  # 你的包名
    version="0.1.0",          # 版本号
    packages=find_packages(),
    install_requires=[        # 依赖项
        "gpustat",             # GPU 状态监控工具
        "jq",                  # JSON 解析工具
    ],
    entry_points={            # 可执行脚本
        'console_scripts': [
            'gpu-memory-alert = scripts.gpu_memory_notify:main',  # 定义主脚本入口
        ],
    },
    author="Your Name",  # 你的名字
    author_email="your_email@example.com",  # 你的电子邮件
    description="A tool to monitor GPU memory usage and send alerts.",  # 简短描述
    long_description=open('README.md').read(),  # 详细描述来自 README.md
    long_description_content_type="text/markdown",  # 说明 README 格式
    url="https://github.com/yourusername/gpu-memory-alert",  # 项目地址
    classifiers=[  # 选择器，帮助用户找到你的包
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python 版本要求
)
