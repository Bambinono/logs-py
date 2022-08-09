
    

file = open("log.txt","r").read()
lista=file.split("commit")
var = lista[12]
var2 = var.split("Date:")
var3 = var2[1]
var4 = var3.split('\n')
print(var4[2])


