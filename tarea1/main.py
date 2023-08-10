from ListaEnlazada import ListaEnlazada
from Persona import Persona


def main():
    lista_personas = ListaEnlazada()

    persona1 = Persona(1, "Juan", 19)
    persona2 = Persona(2, "Jacobo", 20)
    persona3 = Persona(3, "Darlin", 17)
    persona4 = Persona(4, "Doris", 22)

    lista_personas.insertar_ordenado(persona1)
    lista_personas.insertar_ordenado(persona2)
    lista_personas.insertar_ordenado(persona3)
    lista_personas.insertar_ordenado(persona4)

    actual = lista_personas.inicio
    while actual is not None:
        print(f"ID: {actual.persona.id}, Nombre: {actual.persona.nombre}, Edad: {actual.persona.edad}")
        actual = actual.siguiente

if __name__ == "__main__":
    main()