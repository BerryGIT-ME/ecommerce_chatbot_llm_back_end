import os
from openai_client import client

api_key = os.getenv('OPEN_AI_API_KEY')


def ai_chat(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *messages
        ]
    )

    return response.choices[0].message.content