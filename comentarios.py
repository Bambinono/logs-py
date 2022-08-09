file = open("log.txt","r").read()
lista=file.split("Author:")
#print(lista[0:2])
lista_coment = []
for texto in lista[1:]:
    var2 = texto.split("Date:")
    var3 = var2[1]
    var4 = var3.split('\n')
    var5 = var4[1:]
    sin_comentario = ''
    for j in range(len(var5)):
        if 'commit' in var5[j]:
            #print(f'es el elmen xxxxxxx{var5[j]}, y el ant {var5[:j]}, todo es {var5}')
            sin_comentario = var5[:j]
    
    if  sin_comentario !='':
        lista_coment.append(''.join(sin_comentario))   
    else:
        lista_coment.append(''.join(var5))
print(lista_coment)
print(len(lista_coment))

# Funcionando
# file = open("log.txt","r").read()
# lista=file.split("commit")
# var = lista[56]
# var2 = var.split("Date:")
# var3 = var2[1]
# var4 = var3.split('\n')
# print(var4[2])


