class Caminador:
    def comer(self):
        print("caminar")

class Volador:
    def volar(self):
        print("volando")
    
class Nadador:
    def nadar(self):
        print("Nadando")


class Pato(Caminador, Volador, Nadador):
    def grasnar(self):
        print("grasnando")
    
pato = Pato()
pato.grasnar()