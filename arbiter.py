import os
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1263/v1", api_key="not-needed")

# Read the answers from the text file
with open("text.txt", "r") as file:
    ai_answer = file.read().strip()

# Read the question from the text file
with open("question.txt", "r") as file:
    question = file.read().strip()

completion = client.chat.completions.create(
  model="local-model",  # this field is currently unused
  messages=[
    {"role": "system", "content": "You are an AI arbitrator, an expert in everything, who must check the answers of other AIs and leave your short comment. please answer ash short as possible. Don't repeat the answers of other referees. Don't blindly trust other experts, they are often wrong, do your research. User question: {question}"},
    {"role": "user", "content": ai_answer}  # Use the question from the file
  ],
  temperature=0.7,
)

# Сохранение ответа в файл text.txt
with open("text.txt", "a") as file:
    generated_response = completion.choices[0].message.content  # Извлечение текста
    comment = "Expert comment:"
    formatted_text = comment + " " + generated_response
    file.write(formatted_text)
    file.write("\n")  # Добавление новой строки


print(generated_response)
