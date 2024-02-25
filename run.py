import os
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1263/v1", api_key="not-needed")

# Read the question from the text file
with open("question.txt", "r") as file:
    user_question = file.read().strip()

completion = client.chat.completions.create(
  model="local-model",  # this field is currently unused
  messages=[
    {"role": "system", "content": "You are artificial General intelligence."},
    {"role": "user", "content": user_question}  # Use the question from the file
  ],
  temperature=0.7,
)

# Сохранение ответа в файл text.txt
with open("text.txt", "a") as file:
    generated_response = completion.choices[0].message.content  # Извлечение текста
    comment = "Agent opinion:"
    formatted_text = comment + " " + generated_response
    file.write(formatted_text)
    file.write("\n")  # Добавление новой строки

print(generated_response)
