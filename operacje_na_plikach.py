def write():
    wpis = input("""Dodaj wpis: 
""")
    with open('txt.txt', "a") as file:
        plik_read = file.write("\n" + wpis)
        print("zmiana została zapisana pomyślnie")

def read():
    with open('txt.txt', "r") as file:
        plik_read = file.read()
    print("-------")
    print(plik_read)
    print()

def clear():
    with open("txt.txt", "w") as file:
        pass
    print("plik został wyczyszczony poprawnie")
    print("-------")

print("witam w dzienniku Alberta")

while True:
    print("""1 - odczytaj dziennik
2 - dodaj wpis do dziennika
3 - wyczyść dziennik
q - quit""")

    wybor = input("wybierz opcje: ")
    if wybor == "1":
        read()
        
    elif wybor == "2":
        write()

    elif wybor == "3":
        clear()

    elif wybor == "q":
        break
    else:
        print("-----")
        print("nie ma takiej opcji")
        print()