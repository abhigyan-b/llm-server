import os
import json
import requests
import google.generativeai as genai
from google.generativeai.types import ContentType
from PIL import Image
import time

def parse_response(response) -> str:
    try:
        result_text = []
        candidates = response.candidates
        for candidate in candidates:
            content = candidate['content']

            text_parts = content['parts']
            for part in text_parts:
                result_text.append(part['text'])
        return "\n".join(result_text)
    except Exception as e:
        print(e)
        return "Error"


class ChatAssistant:
    def __init__(self, api_key: str):
        # Set up Gemini Pro API details
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def initiate_chat(self, message: str) -> str:
        try:
            # Make the API request
            response = self.model.generate_content(message)
            return response

        except Exception as e:
            print(f"Exception occurred: {e}")
            return f"Error: Exception occurred - {str(e)}"


# Usage example:
# Load the API key and URL from environment variables or a config file
#api_key = os.getenv("GEMINI_API_KEY", "AIzaSyASexqKXuxwqAGNmsed4kYUPkH36Iof6JI")
api_key = os.getenv("GEMINI_API_KEY", "AIzaSyBDYak_MlUlaJw8RzOhLveuxNgjlPuzzRE")
#api_url = os.getenv("GEMINI_API_URL", "")


chat = ChatAssistant(api_key)
msg = input()
response = chat.initiate_chat(msg)
print(response)

