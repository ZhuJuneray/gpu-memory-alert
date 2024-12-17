import os
import yaml
from typing import Dict, Any

class Config:
    def __init__(self, config_path: str = "config/config.yaml"):
        """
        初始化配置类
        Args:
            config_path: 配置文件路径
        """
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """
        加载配置文件
        Returns:
            配置字典
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
            
        with open(self.config_path, 'r') as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise Exception(f"Error parsing configuration file: {e}")
                
    def get_telegram_config(self) -> Dict[str, str]:
        """
        获取Telegram配置
        Returns:
            Telegram配置字典
        """
        return self.config.get('telegram', {})
        
    def get_monitor_config(self) -> Dict[str, int]:
        """
        获取监控配置
        Returns:
            监控配置字典
        """
        return self.config.get('monitor', {})