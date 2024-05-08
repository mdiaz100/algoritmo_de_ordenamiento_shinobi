from AlgoritmodO.Back_shi import MetodoOrdenamiento

class CountingSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        # Obtener el máximo valor del atributo
        max_value = max(getattr(obj, columna) for obj in arr)
        # Obtener el mínimo valor del atributo
        min_value = min(getattr(obj, columna) for obj in arr)

        # Convertir los valores mínimo y máximo a enteros
        min_value = int(min_value)
        max_value = int(max_value)

        # Inicializar el arreglo de conteo
        count = [0] * (max_value - min_value + 1)

        # Contar la frecuencia de cada valor del atributo
        for obj in arr:
            count[int(getattr(obj, columna)) - min_value] += 1

        sorted_arr = []
        # Reconstruir el arreglo ordenado utilizando los conteos
        for i in range(len(count)):
            sorted_arr.extend([obj for obj in arr if int(getattr(obj, columna)) == i + min_value])

        return sorted_arr

# Resumen del Big O:
# Tiempo de ejecución: O(n + k), donde n es el tamaño del arreglo y k es el rango de valores en el arreglo.
# Espacio de memoria: O(n + k)
