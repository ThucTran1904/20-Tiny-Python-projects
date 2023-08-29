def replace_word():
    str = "Hi guys, um Thuk, i'm 20 now and ahi ahi ahi ahi ahi"
    print(str)
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()