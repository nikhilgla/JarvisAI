import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

# print(os.getenv("google_api_key"))


GOOGLE_API_KEY = os.getenv("google_api_key")

genai.configure(api_key=GOOGLE_API_KEY)

model_name = 'gemini-pro'  # or 'gemini-pro-vision' if you want multimodal

model = genai.GenerativeModel(model_name)

def generate_text(prompt):
    """Generates text using the Gemini Pro model."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
prompt = "Write a short poem about a cat."
generated_text = generate_text(prompt)
print(generated_text)

def start_chat():
    """Starts a chat session using the Gemini Pro model."""
    chat = model.start_chat(history=[])  # Initialize with empty history

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Ending chat.")
            break

        try:
            response = chat.send_message(user_input)
            print("Gemini:", response.text)
        except Exception as e:
            print(f"Error during chat: {e}")
            break