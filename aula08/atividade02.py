numeros = []
while True:
    entrada = input("Digite um número (ou 'N' para encerrar): ")
    if entrada.upper() == 'N':
        break                           
    numeros.append(float(entrada))

print(f"Números digitados: {numeros}")
print(f"Quantidade: {len(numeros)}")
