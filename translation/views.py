import os

import openai
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=256,
            temperature=0.5
        )
        chatbot_response = response.choices[0].message['content'].strip()
    return render(request, 'main.html', {'response': chatbot_response})
