import numpy as np
import metodos as mth
M=[]
l=None
h=0
while h==0:
    print("tamaño permitido: ",l)
    k=mth.addcolumna(l)
    M.append(k)
    l=len(k)
    print(k)
    print(l)
    while True:
        YN=input("¿Desea añadir otra fila? S,s o N,n: ")
        if YN=="S" or YN=="s":
            print("Ha Elegido Continuar, tamaño: ",l)
            break
        elif YN=="N" or YN=="n":
            h=1
            break
        else:
            print("¿si o no?")
print("SU MATRIZ ES:")
for t in M:
    print(t)






