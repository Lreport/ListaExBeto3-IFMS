def reverter_caracteres(s):
    if len(s) <= 1:
        return s
    else:
        return reverter_caracteres(s[1:]) + s[0]

text = input('Digite uma string: ')
print(reverter_caracteres(text))