def addcolumna(l):
    print("ok añadiremos una fila :)",l)
    i=1
    m=[]
    while i!=0:
        if l is not None and len(m) == l:
            print("Has alcanzado el límite de tamaño de la lista.")
            print("retornando: ",m,l)
            return(m)
        try:
            print("Para detenerte tipea la letra S o s")
            n=input("inserta el numero: ")
            n=int(n)
            m.append(n)
            
        except:
            print(n)
            if n=="S" or n=="s":
                print("retornando: ",m)
                return(m)
            else:
                print("Debes tipear S o s")
def insFormula():
    print("al Insertar la formula a manipular tenga en cuenta:")
    print("para referenciar una Fila use #(fila) Ej: F1=#1")
    print("Use : para separ primero la Fila afectada de la operacion a realizar Ej: #1:6#2+2#3")
    Fmla="#3:2#2-#3" #input("Inserte la formula: ")
    Typs=[]
    for d in Fmla:
        try:
            d=int(d)
        except:
            d=d
        tipo=type(d)
        Typs.append(tipo)
    return(Fmla,Typs)
    

def idoperaciones(frmla):
    print(frmla)
    ln=len(frmla[0])
    print(ln)
    for t in range(ln):
        print("caracter: ",frmla[0][t],"es un: ",frmla[1][t])
        #para despues haga: buscaremos el : y extraeremos lo que hay entre el # y el : que sera la fila afectada
        #busca el primer numeral para luego extraer su caracter anterior y posterior y lo mandaremos a otra variable
        # haremos lo mismo con el segundo numeral
        #al hacer lo anterior en frmla[0] deberia quedar solo el operador +,- ese lo añadiremos a otra vaiable y devolveremos todo eso
        #maso asi: si la formula insertada es:#1:6#2+2#3 las variables serian: FA=1/op1=[6,2] op2=[2,3]/oprndo=+