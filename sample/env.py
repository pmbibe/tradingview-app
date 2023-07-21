import os
from dotenv import load_dotenv
load_dotenv()
SELENIUM_REMOTE_URL = os.getenv('SELENIUM_REMOTE_URL')
REMOTE_LINK = os.getenv('REMOTE_LINK')
IMAGE_PATH = os.getenv('IMAGE_PATH')