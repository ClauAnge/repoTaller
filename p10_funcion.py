#Ejemplo de aplicacion y creacion de funciones primero creada y despues se aplica 

'''def suma(a,b):
    return a+b'''
#aqui estoy llamando a la funcion pero de manera externa en otro archivo llamado mylibreria
import mylibreria 

if __name__ == "__main__":
    print("resutaldo: ", mylibreria.suma(5,6))
    print("resutaldo: ", mylibreria.suma('5','6'))