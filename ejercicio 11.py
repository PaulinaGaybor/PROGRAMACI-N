

de  randint de importación aleatoria  
mientras que  es cierto :
 filas = int ( input ( "Ingrese el numero de filas:" ))
 columna = int ( input ( "Ingrese el numero de columnas:" ))
 imprimir ( "" )
 si  filas < 4  o  filas > 30 :
        print ( "Las filas deben ser menores que 30 y mayores que 4" )
        
 elif  columna < 4  o  columna > 30 :
         print ( "Las columnas deben ser menores que 30 y mayores que 4" )
         
 más :
     descanso 
 
     
vector = [ 0 ] * filas
para  i  en  rango ( filas ):
    vector [ i ] = [ 0 ] * columna

para  j  en  rango ( filas ):
   para  k k en el  rango ( columna ):
    t = aleatorio ( 0 , 1000 )
    vector [ j ][ k ] = t  

para  h  en  rango ( filas ):
   para  y  en el  rango ( columna ):
       imprimir ( vector [ h ][ y ], end = " " )
   imprimir ( "" )   

imprimir ( " " )
nmayor = 0
para  g  en  rango ( filas ):
    para  t  en el  rango ( columna ):
        si  el vector [ g ][ t ] > nmayor :
            nmayor = vector [ g ][ t ]
            f = gramo
            c = t
print ( "El número" , vector [ f ][ c ], "es el mayor y se encuentra en la posición[" , f , "]" "[" , c , "]" )   