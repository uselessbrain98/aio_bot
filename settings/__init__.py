from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access the variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# HOST = os.getenv('HOST')
# PORT = os.getenv('PORT')
# USER = os.getenv('USER')
# PASSWORD = os.getenv('PASSWORD')
# DB_NAME = os.getenv('DB_NAME')
