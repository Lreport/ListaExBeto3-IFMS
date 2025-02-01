def contar_caracteres(s, c):
    if s and s[0].lower() == c.lower():
        return 1 + contar_caracteres(s[1:], c)
    elif not s:
        return 0
    else:
        return contar_caracteres(s[1:], c)

print(contar_caracteres('Elefante', 'e'))