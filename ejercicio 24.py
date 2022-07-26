f = 1
h = 1
norte = t = 0	
mientras que  n <= 0 :
	n = int ( input ( "Ingrese el número de filas" ))
mientras que  t <= 0 :
	t = int ( input ( "Ingrese el numero de columnas: " ))

mientras  h <= n :
ñ = int ( input ( "Ingrese los valores de la primera fila:" ))
 h += 1
mientras que  f <= t :
 k = int ( input ( "Ingrese los valores de la primera columna:" ))  
 f += 1
        
imprimir ( " | " , fin = " \t " )
para  i  en  rango ( 1 , t + 1 ): 	
 	
 imprimir (f" \t {ñ} ",end=" \t ",)
    
imprimir ()	

para  i  en  rango ( 1 , t * 10 ):  
	imprimir("-",final="")
impresión()	

para i en el rango (1, n + 1):
 	imprimir("\n",k,"|",final="\t")
 	para j en rango (1,t+1):
	  imprimir(redondear((ñ*k),1),final="\t")