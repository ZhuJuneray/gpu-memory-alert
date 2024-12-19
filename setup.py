from setuptools import setup, find_packages

setup(
    name="gpu-memory-alert",  # Your package name
    version="0.1.0",          # Version number
    packages=find_packages(),
    install_requires=[        # Dependencies
        "gpustat",             # GPU status monitoring tool
        "jq",                  # JSON parsing tool
    ],
    entry_points={            # Executable scripts
        'console_scripts': [
            'gpu-memory-alert = scripts.gpu_memory_notify:main',  # Define the main script entry point
        ],
    },
    author="Your Name",  # Your name
    author_email="your_email@example.com",  # Your email
    description="A tool to monitor GPU memory usage and send alerts.",  # Short description
    long_description=open('README.md').read(),  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Specify the format of the README
    url="https://github.com/yourusername/gpu-memory-alert",  # Project URL
    classifiers=[  # Classifiers help users find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python version requirement
)
