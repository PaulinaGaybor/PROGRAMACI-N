de  randint de importación aleatoria  



def  Vali ( T ):
    si  T <  4  o  T  >  30 :
        volver  falso
    más :
        devuelve  Verdadero  y  T
def  Aleatorio ( m , T ):
 para  i  en  rango ( T ):
    r = randint ( 10 , 100 )
    metro [ yo ] = r
 volver  m 

def  prim ( m , f , T ):
    c = 0
    para  j  en  rango ( T ):
        si  m [ j ] % 2 != 0  y  m [ j ] % 3 != 0 :
          F. _ añadir ( v [ j ])
    volver  f


mientras que  es cierto :
    f =  int ( input ( 'Ingrese la dimensión del vector: ' ))
       
    Vali ( f )
    si  Vali ( f ) == Falso :
            print ( 'El valor debe estar dentro del limite de 4 a 30' )
            imprimir ( ' \n ' )
    más :
            descanso
v = [ 0 ] * f    
Aleatorio ( v , f )
print ( "El vector original es:" )
imprimir ( "" )

para  i  en el  rango ( f ):
     imprimir ( "|" , v [ i ], "|" , end = " " )
imprimir ( "" )

pag = []  
primitivo ( v , p , f )
imprimir ( "" )
print ( "El vector con numeros primos es: " )
imprimir ( "" )
para  i  en  rango ( len ( p )):
     imprimir ( "|" , p [ i ], "|" , end = " " ) 