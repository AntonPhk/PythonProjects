print('Программа шифровки / дешифровки текста по методу Цезаря')
k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ) '))
en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]


def cezar(text, k):
    result = []
    if text[0] in en_alphabet:
        alphabet = en_alphabet
        letters_count = 26
    else:
        alphabet = ru_alphabet
        letters_count = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                result.append(alphabet[(alphabet.index(text[i]) + k) % letters_count])
            else:
                result.append(alphabet[(alphabet.index(text[i]) + k) % letters_count + letters_count])
        else:
            result.append(str(text[i]))
    return print(''.join(result))


txt = input('Введите текст ')

cezar(txt)


