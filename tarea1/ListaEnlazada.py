from Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar_ordenado(self, persona):
        nuevo_nodo = Nodo(persona)
        
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
            return
        
        actual = self.inicio
        while actual is not None and actual.persona.edad <= persona.edad:
            actual = actual.siguiente
        if actual is None:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = actual
            nuevo_nodo.anterior = actual.anterior
            actual.anterior = nuevo_nodo
            if nuevo_nodo.anterior is not None:
                nuevo_nodo.anterior.siguiente = nuevo_nodo
            else:
                self.inicio = nuevo_nodo