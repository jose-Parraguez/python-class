class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

    #Para saber si son  iguales las cordenadas
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    

    def __lt__(self,otro):
        return self.lat + self.lon < otro.lat + otro.lon
    
    def __le__(self,otro):
        return self.lat + self.lon <= otro.lat + otro.lon

cordenada = Coordenadas(45, 27)
cordenada2 = Coordenadas(45, 27)

#si imprimo sin metodo magico, compara unidades de memoria 
print(cordenada == cordenada2)
print(cordenada < cordenada2)
print(cordenada <= cordenada2)