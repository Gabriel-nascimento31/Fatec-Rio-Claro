n = int(input('Digite um número: '))
print(f'Os números primos de 1 a {n} são: ')

for r in range(2, n + 1):
    primo = True
    for j in range(2, r):
        if (r % j) == 0:
            primo = False
            break
    if primo:
        print(r)


        
        
