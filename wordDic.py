# Currently, I can't install PyDictionary lib so i run it on GG colab and paste it into this file
# !pip install PyDictionary (run this command too)
from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
  word = input("Enter your word: ")
  if word == '':
    break

  print(dictionary.meaning(word))