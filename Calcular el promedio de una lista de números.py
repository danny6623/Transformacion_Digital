
def calcular_promedio(numeros: list) -> float:
  
    # Validar que la lista no esté vacía
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    # Validar que todos los elementos sean numéricos
    for elemento in numeros:
        if not isinstance(elemento, (int, float)):
            raise TypeError(
                f"Todos los elementos deben ser numéricos. "
                f"Se encontró: {type(elemento).__name__}"
            )

    # Calcular y retornar el promedio
    total = sum(numeros)
    cantidad = len(numeros)
    promedio = total / cantidad

    return promedio


if __name__ == "__main__":

    # Ejemplo 1: lista de calificaciones
    calificaciones = [8.5, 9.0, 7.5, 10.0, 6.5]
    resultado = calcular_promedio(calificaciones)
    print(f"Calificaciones: {calificaciones}")
    print(f"Promedio: {resultado:.2f}\n")

    # Ejemplo 2: lista de temperaturas
    temperaturas = [22.3, 24.1, 19.8, 23.5, 21.0]
    resultado2 = calcular_promedio(temperaturas)
    print(f"Temperaturas (°C): {temperaturas}")
    print(f"Temperatura promedio: {resultado2:.2f} °C\n")

    # Ejemplo 3: manejo de error con lista vacía
    try:
        calcular_promedio([])
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")