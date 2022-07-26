de  randint de importación aleatoria  
desde el  tiempo de  importación del  sueño
def  ordenar ( az ):
    l = largo ( az ) - 1
    para  u  en el  rango ( 0 , l ):
        para  j  en el  rango ( 0 , l ):
            si  az [ j ] > az [ j + 1 ]:
             au = az [ j ]
             az [ j ] = az [ j + 1 ]
             az [ j + 1 ] = au
            
    volver  az            

mientras que  es cierto :
 n = int ( input ( "Ingrese el tamaño del vector:" ))
 si  n < 0 :
  print ( "El arreglo debe ser mayor de 1" )  
 más :
  descanso   
L = [ 0 ] * norte

para  h  en el  rango ( 0 , n ):
    i = randint ( 50 , 100 )
    L [ h ] = yo
  
print ( "Los valores antes de ser ordenados son:" )
 
para  h  en el  rango ( 0 , n ):
    dormir ( 1 )
    print ( " El valor en la posición" , h + 1 , "es:" , L [ h ])
imprimir ( "" )      
print ( "Dando el vector :" )
para  h  en el  rango ( 0 , n ):
    dormir ( 1 )
    imprimir ( "" , L [ h ], fin = " " )
imprimir ( "" )        

dormir ( 1 )
imprimir ( "" )
print ( "Los valores ordenados son :" )
imprimir ( "" )
ordenar ( L )   
para  y  en el  rango ( 0 , n ):
    dormir ( 1 )
    print ( "El vector ordenado en la posición" , y + 1 , "es:" , L [ y ])
imprimir ( "" )        

print ( "Dando el vector :" )
para  y  en el  rango ( 0 , n ):
     dormir ( 1 )
     imprimir ( "" , L [ y ], fin = " " )
imprimir ( "" )      