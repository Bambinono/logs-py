file = open("log.txt","r").read()
lista=file.split("commit")
for texto in lista:
    var2 = texto.split("Date:")
    var3 = var2[1]
    var4 = var3.split('\n')
    print(var4)
    

# Funcionando
# file = open("log.txt","r").read()
# lista=file.split("commit")
# var = lista[56]
# var2 = var.split("Date:")
# var3 = var2[1]
# var4 = var3.split('\n')
# print(var4[2])


