produtos = []

for i in range(5):
    produto = input(f"Digite o nome do produto : ")
    produtos.append(produto) # Adicionas os produtos digitados na lista produtos
print(produtos)

#Acesso ao elemento
n = int(input("Digite a posição do elemento que deseja acessar : "))
print(produtos[n-1]) # Como o indice comça do 0, as vezes a pessoas quer acessar o elemento 1, mas na lista ele está no indice 0, por isso subtraimos 1 do valor digitado.  


#Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f"Digite o novo nome do produto na posição {n}: ")

print(produtos) 

#removendo um elemento da lista
produto_a_remover = input("Digite o nome do produto que deseja remover da lista : ")


if produto_a_remover in produtos:
    produtos.remove(produto_a_remover) # Remove o elemento digitado da lista produtos
print(produtos)