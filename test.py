from google import genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Only used to check API key works or not
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = client.models.list()

    print("✅ API Key is working!\n")
    print("Available Models:\n")

    for model in models:
        print(model.name)

except Exception as e:
    print("❌ Error:")
    print(e)