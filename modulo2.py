nome = "Jose"
idade = 23
altura = 1.34
estudo_py = False

array = [nome, idade, altura, estudo_py]
i = 0

while estudo_py == False:
    print(type(array[i]))
    i += 1
    if i > 3:
        estudo_py = True

idade = "vinte e tres"

print(idade)
print(array[1])


#teste f-string

#errado - print("O "+nome+" tem"+" e"+altura+"m de altura")

print(f"o nome eh {nome} e tem {altura}m de altura")

#input e conversao

nome = input("digite o seu nome\n")
print("")
idade = input("digite sua idade\n")
print(f" {nome} daqui a 10 anos voce tera {int(idade)+10} anos")

#slicing

texto = "programacao"
print(texto[0],texto[-1],texto[0:3],texto[3:],texto[::-1])