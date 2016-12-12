import json

class Clientes:  
    cliente = []

    def read(self):
        with open('clientes.json','r') as file:
            cliente = json.load(file)
            self.data = cliente['results'] 

    def getClientes(self): 
        clientes = []
        for row in self.data:
            cliente = row['nombre']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes

    
                
class Peliculas:  
    pelicula = []

    def read(self):
        with open('peliculas.json','r') as file:
            pelicula = json.load(file)
            self.data1 = pelicula['results'] 

    def getPeliculas(self): 
        peliculas = []
        for row in self.data1:
            pelicula = row['nombre']
            if pelicula not in peliculas:
                peliculas.append(pelicula)
        return peliculas