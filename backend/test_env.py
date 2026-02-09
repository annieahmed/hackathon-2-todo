import os
from dotenv import load_dotenv

load_dotenv()
print("DATABASE_URL from environment:", os.getenv("DATABASE_URL"))