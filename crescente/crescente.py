arq = open("crescente/crescente.txt", "w")

for elemento in range(1, 100 + 1):
    arq.write(str(elemento) + ";")

arq.close()


#PROGRAMA FEITO COM QUEBRA DE LINHAS

# arq = open("crescente.txt", "w")

# for elemento in range(1, 100 + 1):
#     arq.write(str(elemento) + ";\n")

# arq.close()


