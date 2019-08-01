try:
	numero1=5
	numero2=2
	division=numero1/numero2
except ZeroDivisionError:
	print("erro,division entre cero")
except:
	 print("ha habido un error")
else:
	print("operacion exitosa")
finally:
	print("esta prueba del try a terminado")