from tabulate import tabulate
def crearMaquina():
    estados = eval(input("Ingrese lista de estados (ej:['q1','FIN'] => "))
    pasos = eval(input("Ingrese cantidad de pasos (Maximo 10) "))
    crearFuncion(estados, pasos)

def crearFuncion ( q , p ):
    n_filas = len(q)-1 #le resto el estado FIN
    m_col = 3
    print (n_filas)
    a = [[0] * m_col for i in range(n_filas)]
    count_pasos = 0

    for i in range (0,n_filas):
        a[i][0]= q[i]
        e1 = input("ingrese transicion Entrada: 0, Estado: "+q[i]+" : ")
        a[i][1] = e1
        e2 = input("ingrese transicion Entrada: 1, Estado: "+q[i]+" : ")
        a[i][2] = e2
        count_pasos = i+1
    print(tabulate(a,headers=['0', '1'], tablefmt='fancy_grid')) #imprimo la MT como tabla
    print("coutn_pasos"+ str(count_pasos))
    print("pasos por consola"+str(p) )
    if p > count_pasos:
        print("La maquina termino en menos pasos")
        print("Cantidad de pasos"+str(count_pasos)+"pasos colocados por teclado:"+str(p))
    else:
        print("La maquina sigue trabajando")
        print(p)

crearMaquina()
