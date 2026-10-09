import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a helpful AI assistant.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
GEMINI_PRO_MODEL = "gemini-3.5-flash"

JEV_API_KEY = os.getenv("JEV_API_KEY")
JEV_API_URL = "https://api.typesafe.ai/v1/systemone"
COMPLEXITY_THRESHOLD = 0.80
