import requests
from typing import Optional

class TelegramBot:
    def __init__(self, token: str, chat_id: str):
        """
        初始化Telegram机器人
        Args:
            token: 机器人的API token
            chat_id: 接收消息的chat ID
        """
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}"

    def send_message(self, message: str) -> Optional[str]:
        """
        发送消息
        Args:
            message: 要发送的消息内容
        Returns:
            如果发送失败，返回错误信息；否则返回None
        """
        try:
            response = requests.post(
                f"{self.api_url}/sendMessage",
                json={
                    "chat_id": self.chat_id,
                    "text": message,
                    "parse_mode": "HTML"
                }
            )
            response.raise_for_status()
            return None
        except requests.RequestException as e:
            return f"Failed to send message: {str(e)}"

    def test_connection(self) -> bool:
        """
        测试与Telegram API的连接
        Returns:
            连接测试是否成功
        """
        try:
            response = requests.get(f"{self.api_url}/getMe")
            response.raise_for_status()
            return True
        except:
            return False