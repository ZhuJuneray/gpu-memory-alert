import time
from typing import List, Dict, Optional
import pynvml

class GPUMonitor:
    def __init__(self, threshold: int, cooldown: int):
        """
        Initialize the GPU monitor
        Args:
            threshold: GPU memory usage threshold (percentage)
            cooldown: Minimum interval between two alerts (seconds)
        """
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_alert_time = 0
        self._init_nvml()

    def _init_nvml(self):
        """Initialize NVIDIA Management Library (NVML)"""
        try:
            pynvml.nvmlInit()
        except pynvml.NVMLError as e:
            raise Exception(f"Failed to initialize NVML: {e}")

    def _get_gpu_info(self) -> List[Dict[str, float]]:
        """
        Get memory usage information for all GPUs
        Returns:
            A list of GPU information, each element contains device ID and memory usage percentage
        """
        gpu_info = []
        device_count = pynvml.nvmlDeviceGetCount()
        
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
            
            # Calculate memory usage percentage
            usage_percent = (memory.used / memory.total) * 100
            gpu_info.append({
                'device_id': i,
                'memory_usage': usage_percent
            })
            
        return gpu_info

    def check_memory(self) -> Optional[str]:
        """
        Check GPU memory usage
        Returns:
            If any GPU memory is below the threshold, return an alert message; otherwise, return None
        """
        current_time = time.time()
        
        # Check if it is within the cooldown period
        if current_time - self.last_alert_time < self.cooldown:
            return None
            
        try:
            gpu_info = self._get_gpu_info()
        except Exception as e:
            return f"Error getting GPU information: {e}"
            
        # Check if there are GPUs with memory usage below the threshold
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
        """Clean up NVML"""
        try:
            pynvml.nvmlShutdown()
        except:
            pass
