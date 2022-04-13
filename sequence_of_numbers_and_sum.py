valores, somas, valor = [], [], []

while True:
  m, n = map(int, input().split())  
  if m <= 0 or n <= 0:    # m ou n é negativo ou igual a zero 
    break
  else:     
    if m > n:             #contrução da sequência
      for i in range(n, m + 1):        
        valor.append(i)        
    elif m < n:
      for i in range(m, n +1):
        valor.append(i)
    somas.append(sum(valor))
    valor = str(valor)[1:-1].replace(', ', ' ')
    valores.append(valor)
    valor = []

for i in range(len(valores)):
  print(f'{valores[i]} Sum={somas[i]}')