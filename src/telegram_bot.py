import requests
from typing import Optional

class TelegramBot:
    def __init__(self, token: str, chat_id: str):
        """
        Initialize the Telegram bot
        Args:
            token: The bot's API token
            chat_id: The chat ID to receive messages
        """
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}"

    def send_message(self, message: str) -> Optional[str]:
        """
        Send a message
        Args:
            message: The content of the message to send
        Returns:
            If sending fails, returns an error message; otherwise, returns None
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
        Test the connection to the Telegram API
        Returns:
            Whether the connection test was successful
        """
        try:
            response = requests.get(f"{self.api_url}/getMe")
            response.raise_for_status()
            return True
        except:
            return False
