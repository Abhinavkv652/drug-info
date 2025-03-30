import pandas as pd
from IPython.display import display
import ipywidgets as widgets
import openai

openai.api_key = "your-api-key-here"

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Fixed model name
            messages=[
                {"role": "system", "content": "You are a medical assistant specializing in drug information."},
                {"role": "user", "content": prompt}
            ]
        )
        if response.choices and response.choices[0].message and response.choices[0].message.content:
            return response.choices[0].message.content.strip()
        return "No response received"
    except Exception as e:
        return f"Error: {str(e)}"

def check_drug_info(prompt, drug_data):
    for drug in drug_data["Common Name"]:
        if drug.lower() in prompt.lower():
            drug_index = drug_data["Common Name"].index(drug)
            print(f"\nDrug Information for {drug}:")
            for key in drug_data.keys():
                print(f"{key}: {drug_data[key][drug_index]}")
            return True
    return False

if __name__ == "__main__":
    print("Hello! I am a medical chatbot. Ask me about drugs and their effects.")
    
    drug_data = {
        "Common Name": ["Aspirin", "Quinine", "Morphine"],
        "Chemical Name": ["Acetylsalicylic Acid", "C20H24N2O2", "C17H19NO3"],
        "Structure": ["C9H8O4", "C20H24N2O2", "C17H19NO3"],
        "Advantages": [
            "Reduces pain, fever, and inflammation",
            "Used to treat malaria",
            "Effective pain relief for severe pain"
        ],
        "Disadvantages": [
            "May cause stomach irritation or bleeding",
            "Can cause side effects like tinnitus and nausea",
            "Highly addictive and can lead to dependency"
        ]
    }

    while True:
        prompt = input("You: ")
        if prompt.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Goodbye! Have a great day.")
            break
            
        # Check if the prompt contains any drug names from our database
        if not check_drug_info(prompt, drug_data):
            response = chat_with_gpt(prompt)
            print("Bot:", response)