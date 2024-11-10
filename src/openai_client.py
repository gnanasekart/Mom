from openai import OpenAI
import ollama

MODEL_NAME = "mistral"
BASE_URL = "http://localhost:11434/api/generate -d"
API_KEY = "ollama"

client = ollama(
    base_url = BASE_URL,
    api_key=API_KEY, # required, but unused
)

def get_contents(transcription, SYSTEM_PROMPTS):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,
        messages=[
            {   "role": "system",
                "content": SYSTEM_PROMPTS
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

