import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
CANDIDATE_KEY = os.getenv("CANDIDATE_KEY")