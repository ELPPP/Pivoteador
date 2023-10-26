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
