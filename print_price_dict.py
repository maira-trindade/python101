codigo_preco = {'1':4.00, '2':4.50, '3':5.00, '4':2.00, '5':1.50}
codigo, qtdd = input().split(' ')

total = int(qtdd) * (codigo_preco[codigo])
print(f'Total: R$ {total:.2f}')