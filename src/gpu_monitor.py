import time
from typing import List, Dict, Optional
import pynvml

class GPUMonitor:
    def __init__(self, threshold: int, cooldown: int):
        """
        初始化GPU监控器
        Args:
            threshold: GPU内存使用率阈值（百分比）
            cooldown: 两次告警之间的最小间隔（秒）
        """
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_alert_time = 0
        self._init_nvml()

    def _init_nvml(self):
        """初始化NVIDIA Management Library"""
        try:
            pynvml.nvmlInit()
        except pynvml.NVMLError as e:
            raise Exception(f"Failed to initialize NVML: {e}")

    def _get_gpu_info(self) -> List[Dict[str, float]]:
        """
        获取所有GPU的内存使用情况
        Returns:
            GPU信息列表，每个元素包含设备ID和内存使用率
        """
        gpu_info = []
        device_count = pynvml.nvmlDeviceGetCount()
        
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
            
            # 计算内存使用率
            usage_percent = (memory.used / memory.total) * 100
            gpu_info.append({
                'device_id': i,
                'memory_usage': usage_percent
            })
            
        return gpu_info

    def check_memory(self) -> Optional[str]:
        """
        检查GPU内存使用情况
        Returns:
            如果有GPU内存低于阈值，返回告警消息；否则返回None
        """
        current_time = time.time()
        
        # 检查是否在冷却期
        if current_time - self.last_alert_time < self.cooldown:
            return None
            
        try:
            gpu_info = self._get_gpu_info()
        except Exception as e:
            return f"Error getting GPU information: {e}"
            
        # 检查是否有GPU内存使用率低于阈值
        low_memory_gpus = [
            info for info in gpu_info 
            if info['memory_usage'] < self.threshold
        ]
        
        if low_memory_gpus:
            self.last_alert_time = current_time
            message = "🚨 Low GPU Memory Alert:\n\n"
            for gpu in low_memory_gpus:
                message += f"GPU {gpu['device_id']}: {gpu['memory_usage']:.2f}% memory usage\n"
            return message
            
        return None

    def __del__(self):
        """清理NVML"""
        try:
            pynvml.nvmlShutdown()
        except:
            pass