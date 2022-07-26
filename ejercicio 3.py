número = 1
suma_intervalo = 0
contador1 = 0
suma_fuera = 0
contador2 = 0
mientras que  es cierto :
    val1 = int ( input ( 'ingrese el primer valor:' ))
    val2 = int ( input ( 'ingrese el segundo valor: ' ))
    si  val1 == val2 :
        print ( 'los valores no deben ser iguales' )
    más :
        descanso
si  val1 > val2 :
    mínimo = val2
    máximo = val1
más :
    mínimo = val1
    máximo = val2
mientras  numero != 0 :
    numero = int ( input ( 'digite un valor: ' ))
    si  numero > minimo  y  numero < maximo :
        suma_intervalo += número
    elif  numero < minimo  o  numero > maximo :
        suma_fuera += numero
        contador1 += 1
    elif  numero == minimo  or  numero == maximo :
        contador2 += 1
    print ( 'la suma de los numeros que estan dentro es: ' , suma_intervalo )
    print ( 'el promedio de los numeros que estan fuera es: ' , suma_fuera / contador1 )
    print ( 'la cantidad de numeros ingresados ​​es igual a los limites' , contador2 )
    print ( 'fin del algoritmo' )