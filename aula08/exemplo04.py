#set "Conjuntos"
# Coleção mutavel
# Não garante a ordem dos elementos
# Não há indices, não é possível acessar os elementos por indices

#Criar sets vazios

dias = set() 
dias.add('Segunda-feira') # Adiciona um elemento ao set
dias.add('Terça-feira') # Adiciona um elemento ao set   
print(dias) # Imprime os elementos do set

#Conjuntos inicializados
frutas = {'Maça', 'Uva', 'Pera', 'Laranja'}
print(frutas) # Imprime os elementos do set

#Remover um elemento do set
frutas.remove('Uva') # Remove o elemento do set, tambem podemos usar o metodo discard, que não gera erro caso o elemento não exista no set
print(frutas) # Imprime os elementos do set
print(len(frutas)) # Imprime a quantidade de elementos do set