def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

# Exemplo de uso:
string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
