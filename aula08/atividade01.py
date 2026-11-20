vendas = [0] * 10            
for i in range(10):
    vendas[i] = float(input("Digite o valor das vendas : "))
total_vendas = sum(vendas)
print(f"Total de vendas: {total_vendas}")
print(f"Valores das vendas: {vendas}")