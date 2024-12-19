import os
import yaml
from typing import Dict, Any

class Config:
    def __init__(self, config_path: str = "config/config.yaml"):
        """
        Initialize the configuration class
        Args:
            config_path: The path to the configuration file
        """
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """
        Load the configuration file
        Returns:
            A dictionary representing the configuration
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
        Get the Telegram configuration
        Returns:
            A dictionary representing the Telegram configuration
        """
        return self.config.get('telegram', {})
        
    def get_monitor_config(self) -> Dict[str, int]:
        """
        Get the monitoring configuration
        Returns:
            A dictionary representing the monitoring configuration
        """
        return self.config.get('monitor', {})
