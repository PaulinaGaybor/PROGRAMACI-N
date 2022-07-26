def  primo ( n ):
    c  =  0
    para  i  en  rango ( 1 , n + 1 ):
        si  n %  i == 0 :
            do += 1
    si  c == 2 :
       volver  verdadero
    más :
        volver  falso

para  k  en  rango ( 1 , 20 ):
     si  primo ( k + 1 ):
         imprimir ( k + 1 , fin = " " )
         
imprimir ()       