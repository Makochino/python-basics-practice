word = input("Введите слово: ")  
word_list = list(word)  
word_reverse = ""  


for i in range(len(word_list) -1, -1, -1):  
    word_reverse += word_list[i] 

print(f"Перевернутое слово: {word_reverse}")  