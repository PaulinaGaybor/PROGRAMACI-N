importar  al azar
 tiempo de importación

def  Burbuja ( arreglo ):
    n  =  len ( arreglo )

    para  i  en  rango ( n - 1 ):
        para  j  en  rango ( n - i - 1 ):
            if  arreglo [ j ] >  arreglo [ j + 1 ]:
                arreglo [ j ], arreglo [ j + 1 ] =  arreglo [ j + 1 ], arreglo [ j ]
                
 
n = int ( input ( 'Ingrese el tamaño del vector: ' ))
Vector  = [ 0 ] * n
para  i  en  rango ( n ):
    V = ( aleatorio . randint ( 50 , 100 ))
    Vector [ i ] = V
print ( "El vector original es :" )
imprimir ( Vector )
tiempo _ dormir ( 1 )
Burbuja ( Vector )
print ( 'El vector oredenado es:' )
imprimir ( Vector )
