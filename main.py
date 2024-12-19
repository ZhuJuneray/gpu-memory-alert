import time
import logging
from src.config import Config
from src.gpu_monitor import GPUMonitor
from src.telegram_bot import TelegramBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Load configuration
        config = Config()
        telegram_config = config.get_telegram_config()
        monitor_config = config.get_monitor_config()
        
        # Initialize the Telegram bot
        bot = TelegramBot(
            token=telegram_config['bot_token'],
            chat_id=telegram_config['chat_id']
        )
        
        # Test Telegram connection
        if not bot.test_connection():
            raise Exception("Failed to connect to Telegram API")
            
        # Initialize the GPU monitor
        monitor = GPUMonitor(
            threshold=monitor_config['threshold'],
            cooldown=monitor_config['cooldown']
        )
        
        logger.info("GPU Memory Alert System Started")
        bot.send_message("🟢 GPU Memory Alert System is now running")
        
        # Main loop
        while True:
            # Check GPU memory
            alert_message = monitor.check_memory()
            # bot.send_message("🔄 Checking GPU memory...")
            
            # Send alert if necessary
            if alert_message:
                error = bot.send_message(alert_message)
                if error:
                    logger.error(error)
                    
            # Wait for the next check
            time.sleep(monitor_config['check_interval'])
            
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    main()
