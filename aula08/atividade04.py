numero = []
for i in range(15):
    numero.append(int(input("Digite os números : ")))

sem_repetir = list(set(numero)) # Remove os elementos repetidos da lista numero
print(sem_repetir)