import os
import tkinter as tk
import subprocess

# Удаление файла text.txt
if os.path.exists("text.txt"):
  os.remove("text.txt")

def run_script(num_times):
  """
  Запускает скрипт run.py n раз.
  """
  for i in range(num_times):
    subprocess.run(["python", "run.py"])
  # Запуск arbiter.py
  for i in range(num_times):
    subprocess.run(["python", "arbiter.py"])
  # Запуск superexpert.py один раз
  subprocess.run(["python", "superexpert.py"])

def main():
  """
  Создает интерфейс tkinter и запускает run.py.
  """
  root = tk.Tk()
  root.title("Запуск скрипта run.py")

  # Метка для ввода количества повторений
  label = tk.Label(text="Number of Agents and Experts (agents answer independently, experts answer depending on all answers:")
  label.pack()

  # Поле ввода
  entry = tk.Entry()
  entry.pack()

  # Кнопка запуска
  button = tk.Button(text="Start", command=lambda: run_script(int(entry.get())))
  button.pack()

  root.mainloop()

if __name__ == "__main__":
  main()
