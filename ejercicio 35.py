de  randint de importación aleatoria  
mientras que  es cierto :
    x = int ( input ( "Ingrese la cantidad de filas:" ))
    y = int ( input ( "Ingrese la cantidad de columnas:" ))
    si  x < 4  o  x > 30 :
        print ( "Las filas no pueden ser menores que 4 ni mayores de 30" )
    elif  y < 4  o  y > 30 :
        print ( "Las columnas no pueden ser menores que 4 ni mayores de 30" )
    más :
        descanso
z = [ 0 ] * x

para  p  en el  rango ( x ):
    z [ pag ] = [ 0 ] * y

para  p  en el  rango ( x ):
  para  q  en el  rango ( y ):
      n = aleatorio ( 50 , 1000 )
      z [ pag ][ q ] = norte
para  p  en el  rango ( x ):
 para  q  en el  rango ( y ):
  imprimir ( "|" , z [ p ][ q ], "|" , end = " " )
 imprimir ( "" )
imprimir ( "" )

si  x == y :
    print ( "La diagonal principal es:" )


    para  p  en el  rango ( x ):
     para  q  en el  rango ( y ):
      si  p == q :
       imprimir ( "|" , z [ p ][ q ], "|" , end = " " )
      más :
       imprimir ( "|" , "- " , "|" , fin = " " )
     imprimir ( "" )
si  x == y :

    print ( "La segunda diagonal es:" )



para  p  en el  rango ( x ):
 para  q  en el  rango ( y ):
  si  p + q == x - 1 :
   imprimir ( "|" , z [ p ][ q ], "|" , end = " " )
  más :
   imprimir ( "|" , "- " , "|" , fin = " " )
 imprimir ( "" )