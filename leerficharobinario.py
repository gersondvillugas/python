import pickle
fichero=open("fichero_colores.pckl","rb")
lista_leida_fichero=pickle.load(fichero)
print(lista_leida_fichero)
