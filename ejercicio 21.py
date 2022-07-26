mientras que  es ciertoTrue :
    p = intint ( input ( "Ingresar un numero:" ))
    si  p p<= 0 :
        print ( "Los numeros primos solo pueden ser positivos" )
    más :
        descanso

definición  np ( p ):
   
    X = 1
    c = 0
    mientras que  x <= p :
        si  p % x == 0 :
            do += 1
        X + = 1 
    si  c == 2 :
        print ( "El número " , p , "es primo" )
    más :
        print ( "El número " , p , " no es primo" )    
    
np ( pag )    