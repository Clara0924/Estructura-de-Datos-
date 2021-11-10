importar sistema  operativo
de  Arbol  importar  Arbol

# Decidí crear un archivo nuevo (Arbol.py) para esconder el codigo 
# correspondiente a las clases "Arbol" y "Nodo", de modo que el código se viera
# mas limpio y ordenado.


mientras que es  verdadero :
    árbol  =  Arbol ()
    # os.system ("cls")
    imprimir ( "Arbol ABB" )
    opc  =  input ( " \ n 1.-Parte Práctica 1 \ n 2.-Parte Práctica 2 \ n 3.-Salir \ n \ n Elige una opcion ->" )


    # Parte Practica 1 del Parcial # 1
    si  opc  ==  '1' :
        # Estableciendo los nodos por defecto y añadiendolos al arbol
        # vía para en
        nudos  = [ - 5 , 2 , - 11 , 4 , - 13 , 5 , 3 , - 14 , 1 , 6 , 10 , - 12 , 8 ]
        print ( " \ n Nodos a utilizar:" , nodos )
        para  nodo  en  nodos :
            árbol . para contactar ( nodo , nodo )
        
        # Las funciones "buscarNodosHoja" y "buscarNodosConAmbosHijos" son propias de la
        # clase arbol, que se encuentra en el archivo Arbol.py.
        nodosHoja  =  árbol . buscarNodosHoja ( árbol . raiz )
        nodosConAmbosHijos  =  árbol . buscarNodosConAmbosHijos ( árbol . raiz )
        
        # Imprimiendo Resultados
        print ( 'Los Nodos Hoja son>' , nodosHoja )
        print ( 'Los Nodos con ambos hijos son>' , nodosConAmbosHijos )
    
    # Parte Practica 2 del Parcial # 1
    elif  opc  ==  '2' :
        # Estableciendo los nodos por defecto y añadiendolos al arbol
        # vía para en
        nodos  = [ 25 , 12 , 6 , 3 , 9 , 18 , 15 , 21 , 37 , 30 , 43 , 27 , 33 , 40 , 46 ]
        print ( " \ n Nodos a utilizar:" , nodos )
        para  nodo  en  nodos :
            árbol . para contactar ( nodo , nodo )
        
        # Haciendo los tres recorridos> inorden, preorden y postorden.
        imprimir ( ' \ n Recorrido inorden' )
        árbol . inorder ( árbol . raiz )
        
        imprimir ( ' \ n Recorrido preorden' )
        árbol . preorder ( árbol . raiz )
        
        imprimir ( ' \ n Recorrido postorden' )
        árbol . postorder ( árbol . raiz )

    elif  opc  ==  '3' :
        print ( " \ n Elegiste salir ... \ n " )
        os . sistema ( "pausa" )
        rotura
    otra cosa :
        print ( " \ n Elige una opcion correcta ..." )
    imprimir ()
    os . sistema ( "pausa" )
