\wilson bolivar CI 25527330 seccion (2)
\ ejercicio libre 
def multi (A, B):
	multi = A * B
	return multi
def elevar (multi2):
	elevar multi2**2
	return elevar

res = "s"
while res == 's':
	A = input ('ingrese su primer numero')
	B = input ('ingrese se segundo numero')
	print multi (A,B)
	opcines = input ('desea elevar su multiplicacion (1) , si no lo desea (2)')
	if opcines == 1 :
		multi2 = input (multi)
		print elevar (multi2)
	else opcines == 2 :
		print 'su resultado es', multi (A,B)
		res = 'n'
