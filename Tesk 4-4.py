# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество 
# символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно 
# зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию,
# которая спрашивает ключ, считывает текст и дешифровывает его.

def alphabet():
    alphabets_in_capital = []
    for i in range(ord('А'),ord('ѐ')):
        alphabets_in_capital.append(chr(i))
    return alphabets_in_capital

def encrypted_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i - encrypt_number]  
        else: result += char
    return result

def write_text_into_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def read_text_from_file(file_name):
    text = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            text += line
    return text

def unencrypt_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i + encrypt_number]  
        else: result += char
    return result



alphabet = alphabet()
normal_text = read_text_from_file('task_4_normal.txt')
encrypted_text = encrypted_text(normal_text, alphabet, 2)
write_text_into_file('task_4_shifr.txt' ,encrypted_text)
encrypted_text_from_file = read_text_from_file('task_4_shifr.txt')
unencrypted_text = unencrypt_text(encrypted_text_from_file, alphabet, 2)