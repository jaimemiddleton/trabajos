limite_inferior = int(input("cual es el limite inferior?"))
contador = limite_inferior
suma = 0
limite_superior = int(input("cual es el limite superior?"))
if limite_inferior > limite_superior:
        print("el limite inferior es mayor que el limite superior")
else:
        size=len(str(contador))
        while size < 3:
            contador = contador + 1
            size=len(str(contador))
        while contador <= limite_superior:
            unidades= (str(contador))[size-1]
            decenas= (str(contador))[size-2]
            centenas= (str(contador))[size-3]
            if int(unidades) != 0:
                if ((abs(int(centenas) - int(decenas)))% int(unidades))==0:
                    suma =  suma + contador
            contador = contador + 1
		    
print("La suma entre",limite_inferior,"y",limite_superior, "es", suma)
