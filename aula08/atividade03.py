numeros = []            
for i in range(3):
    numero = int(input("Digite os números : "))
    numeros.append(numero)

ordenados = sorted(numeros) # Ordena os elementos da lista do menor para o maior


print(f"Números ordenados: {ordenados}")    