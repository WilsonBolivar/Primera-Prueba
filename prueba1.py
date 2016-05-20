\ejercicios
\1) realize un algoritmo que permita el ingreso de datos por teclado que evalue
\dicha entrada separe la entrada en numeros y letras y imprima por pantalla
\2) es libre
\wilson bolivar CI 25527330 seccion (2)
import re 


def  entrada(en):
	if len (en) and not ('' in en):
		if not re.search('[a,z]',en):
		    return 'los datos deben contener letras'
	    elif en.isalnum():
		    return 'debe conterner numeros y letras'
	else:
		return True 

en = rew_input('ingrese los datos alfanumericos ')
print entrada(en) 

