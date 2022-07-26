mientras que  es cierto :
    n = int ( input ( "Ingrese el número hasta que tabla desee contar:" ))
    k = int ( input ( "Ingrese hasta que número quiera multiplicar" ))
    descanso

p = 0
soy = 0
metro = 0
j = 0
s = 0
h = 1
t = 1
número = 1
mientras que  t <= n :
        print ( "La tabla del " , t , " es:" )
        mientras que  número <= n :
          imprimir ( t , "*" , número , "=" , t * número )    
          número += 1
          
          r = t * número
          s += r
        t += 1
        número -= n
          
        si  r  %  3 ==  0 :
              m += 1
          
        si  r  %  5 ==  0 :
              j += 1
        si  r % 2 == 0 :
              pag += 1
        más :
              soy += 1 
          
           
        print ( "La suma de la tabla del" , n , "es:" , s )
        print ( "El promedio es:" , s / k )
        print ( "Los multiplos de 3 son:" , m )
        print ( "Los multiplos de 5 son:" , j )
        print ( "Hay" , p , "numeros pares" )
        print ( "Hay" , im , "numeros impares" )
        imprimir ( "" )