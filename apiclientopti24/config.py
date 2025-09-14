import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "https://api-demo.opti-24.ru/vip/")
API_KEY = os.getenv("API_KEY")
LOGIN = os.getenv("API_LOGIN")
PASSWORD = os.getenv("API_PASSWORD")

REQUEST_LOG_FILE = os.getenv("REQUEST_LOG_FILE", "./api_requests.jsonl")
LOGGER_FILE = os.getenv("LOGGER_FILE", "./api.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
