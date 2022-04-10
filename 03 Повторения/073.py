# Упражнение 73. Код Цезаря
#
# Одним из первых в истории примеров шифрования считаются закодиро-
# ванные послания Юлия Цезаря. Римскому полководцу необходимо было
# посылать письменные приказы своим генералам, но он не желал, чтобы
# в случае чего их прочитали недруги. В результате он стал шифровать свои
# послания довольно простым методом, который впоследствии стали на-
# зывать кодом Цезаря.
#
# Идея шифрования была совершенно тривиальной и заключалась в цик-
# лическом сдвиге букв на три позиции. В итоге буква A превращалась в D,
# B – в E, C – в F и т. д. Последние три буквы алфавита переносились на на-
# чало. Таким образом, буква X становилась A, Y – B, а Z – C. Цифры и другие
# символы не подвергались шифрованию.
#
# Напишите программу, реализующую код Цезаря. Позвольте пользова-
# телю ввести фразу и количество символов для сдвига, после чего выведите
# результирующее сообщение. Убедитесь в том, что ваша программа шиф-
# рует как строчные, так и прописные буквы. Также должна быть возмож-
# ность указывать отрицательный сдвиг, чтобы можно было использовать
# вашу программу для расшифровки фраз.

import string

# lower_alphabet = string.ascii_lowercase
# upper_alphabet = string.ascii_uppercase
user_string = input("Введите строку для шифрования: ")
user_offset = int(input("Введите смещение: "))
cipher_string = ""

for letter in user_string:
    if letter.isupper():
        l_index = string.ascii_uppercase.index(letter)
        if user_offset + l_index >= 26:
            l_index = user_offset + l_index - 26
        elif user_offset + l_index < 0:
            l_index = user_offset + l_index + 26
        else:
            l_index = user_offset + l_index
        cipher_string += string.ascii_uppercase[l_index]
    elif letter.islower():
        l_index = string.ascii_lowercase.index(letter)
        if user_offset + l_index >= 26:
            l_index = user_offset + l_index - 26
        elif user_offset + l_index < 0:
            l_index = user_offset + l_index + 26
        else:
            l_index = user_offset + l_index
        cipher_string += string.ascii_lowercase[l_index]

print(cipher_string)