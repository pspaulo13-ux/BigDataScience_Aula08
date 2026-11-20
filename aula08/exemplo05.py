#TUPLAS
#Coleção imutavel
#Permite elementos duplicados
#Permite acesso por indices
#Mantém a ordem dos elementos

frutas = ('Maça', 'Uva', 'Pera', 'Laranja')
print(frutas) # Imprime os elementos da tupla
print(frutas[0]) #Acessando o elemento da tupla pelo indice
#Não é possivel alterar, remover ou adicionar elementos em uma tupla, pois ela é imutavel, nesse caso teria que tranformar a tupla em lista, fazer as alterações e depois transformar novamente em tupla.   


numeros = (10, 20, 50, 20, 30, 10, 400,20)
print(numeros.count(20)) # Imprime a quantidade de vezes que o elemento 20 aparece na tupla
