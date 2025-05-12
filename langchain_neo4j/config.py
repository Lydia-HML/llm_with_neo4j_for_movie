import os
from dotenv import load_dotenv
import openai
from langchain.chat_models import init_chat_model
#from langchain_openai import ChatOpenAI
import google.generativeai as genai

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_USERNAME = "neo4j"


#chat_model = init_chat_model("gpt-4o", model_provider="openai")
chat_model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


print(OPENAI_API_KEY)
print(NEO4J_URI)
print(NEO4J_PASSWORD)
