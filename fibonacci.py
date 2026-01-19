x = int(input("Podaj liczbę wyrazów ciągu Fibonacciego: "))

if x == 0:
    lista = []
elif x == 1:
    lista = [0]
else:
    lista = [0, 1]
    for i in range(2, x):
        lista.append(lista[-1] + lista[-2])

print(lista)
