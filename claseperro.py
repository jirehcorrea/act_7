print("programacion poo")
#definicion de clases 
class perro:
    #funciones dentro de la clase 
    nombre="boby"
    edad=4
    def morder(self):
        print("el perro me mordio")
    def dato_perro(self,nombre,edad):
        print(f"nombre : {nombre} edad: {edad}")
#zona de objetos
pitbull=perro()
#zona de uso de objetos
pitbull.dato_perro("boby",4)
pitbull.morder()





