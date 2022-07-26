de  randint de importación aleatoria  

mientras que  es cierto :
 N = int ( input ( "Ingrese el número de filas:" ))

 si  N < 4  o  N > 30 :
  print ( "Las filas no pueden ser menores que 4 ni mayores de 30" )
 más :
  descanso
mientras que  es cierto :

 M = int ( input ( "Ingrese el número de columnas:" ))
 si  M < 4  o  M > 30 :
  print ( "Las columnas no pueden ser menores que 4 ni mayores de 30" )
 más :
  descanso

metro = [ 0 ] * norte

para  i  en el  rango ( N ):
  metro [ yo ] = [ 0 ] * METRO

para  i  en el  rango ( N ):
 para  j  en  rango ( M ):
  h = randint ( 50 , 1000 )
  metro [ yo ][ j ] = h

imprimir ( "" )
print ( "La matriz es:" )
imprimir ( "" )
para  i  en el  rango ( N ):
 para  j  en  rango ( M ):
  imprimir ( "|" , m [ i ][ j ], "|" , end = " " )
 imprimir ( "" )
imprimir ( "" )

si  N == METRO :
 print ( "La diagonal principal es:" )
 imprimir ( "" )

 para  i  en el  rango ( N ):
  para  j  en  rango ( M ):
   si  yo == j :
    imprimir ( "|" , m [ i ][ j ], "|" , end = " " )
   más :
    imprimir ( "|" , "- " , "|" , fin = " " )
  imprimir ( "" )
imprimir ( "" )  
si  N == METRO :

 print ( "La diagonal secundaria es:" )
 imprimir ( "" )
para  i  en el  rango ( N ):
 para  j  en  rango ( M ):
  si  i + j == N - 1 :
   imprimir ( "|" , m [ i ][ j ], "|" , end = " " )
  más :
   imprimir ( "|" , "- " , "|" , fin = " " )
 imprimir ( "" )