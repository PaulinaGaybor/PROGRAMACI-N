def  elnumeroesprimo ( num ):
    contadorprimo  =  0
    para  i  en  rango ( 1 , num + 1 ):
        si  núm %  i == 0 :
            contadorprimo += 1
    si  contadorprimo == 2 :
     volver  verdadero
    más :
     volver  falso

para  o  en  rango ( 1 , 20 ):
     si  elnumeroesprimo ( o + 1 ):
         imprimir ( o + 1 , fin = " " )
         
imprimir ()       