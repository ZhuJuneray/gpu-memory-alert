import time
import logging
from src.config import Config
from src.gpu_monitor import GPUMonitor
from src.telegram_bot import TelegramBot

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # 加载配置
        config = Config()
        telegram_config = config.get_telegram_config()
        monitor_config = config.get_monitor_config()
        
        # 初始化Telegram机器人
        bot = TelegramBot(
            token=telegram_config['bot_token'],
            chat_id=telegram_config['chat_id']
        )
        
        # 测试Telegram连接
        if not bot.test_connection():
            raise Exception("Failed to connect to Telegram API")
            
        # 初始化GPU监控器
        monitor = GPUMonitor(
            threshold=monitor_config['threshold'],
            cooldown=monitor_config['cooldown']
        )
        
        logger.info("GPU Memory Alert System Started")
        bot.send_message("🟢 GPU Memory Alert System is now running")
        
        # 主循环
        while True:
            # 检查GPU内存
            alert_message = monitor.check_memory()
            # bot.send_message("🔄 Checking GPU memory...")
            
            # 如果需要发送告警
            if alert_message:
                error = bot.send_message(alert_message)
                if error:
                    logger.error(error)
                    
            # 等待下一次检查
            time.sleep(monitor_config['check_interval'])
            
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    main()