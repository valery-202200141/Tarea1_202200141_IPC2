from persona import persona
from ListaEnlazada import ListaEnlazada
def main():
    lista_personas = ListaEnlazada()

    persona1 = persona(1, "Alice", 30)
    persona2 = persona(2, "Bob", 25)
    persona3 = persona(3, "Charlie", 40)
    persona4 = persona(4, "David", 22)

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