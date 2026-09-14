import os, time
prewrite = []

def top():
    print("Conversor simples Decimal - Binário : Por Yan Mendes")

def cls():
    os.system("cls")

top()
print("A - 4 bits (0-15), B - 8 bits (0-255), C - 16 bits (0-65535), D - 32 bits (0-4294967296)  *Padrão - D")


while True:
    option = input("Qual o tamanho, em bits, do número traduzido? ")
    if option == "A" or option == "a":
        length = 4
        break
    elif option == "B" or option == "b":
        length = 8
        break
    elif option == "C" or option == "c":
        length = 16
        break
    elif option == "D" or option == "d":
        length = 32
        break
    else:
        length = 32
        print("Opção inválida selecionada. 32 bits definido por padrão.")
        escolha = input("Deseja mudar? S/N: ")
        if escolha == "S" or escolha == "s":
            continue
        else:
            cls()
            print("definição mantida.")
            break


def operador(valor):
    resto = valor%2
    entrada = valor//2
    return resto, entrada

while True:
    try:
        cls()
        top()
        entrada = int(input("Qual o número a ser traduzido? "))
    except ValueError:
        cls()
        top()
        print("Você não digitou um número válido!")
        time.sleep(3)
        continue
    else:
        break

while not (entrada == 0 or entrada == 1):
    resto, entrada = operador(entrada)
    prewrite.append(resto)
    if entrada == 0 or entrada == 1:
        prewrite.append(entrada)

flength = len(prewrite)

if flength > length:
    print("Estouro!!! Excedeu o tamanho de bits!")
    quit()

wrote = ""
write = prewrite[::-1]

for things in write:
    wrote = wrote + str(things)

wrote = wrote.zfill(length)

print(wrote)
