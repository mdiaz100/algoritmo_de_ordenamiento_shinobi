from AlgoritmodO.Back_shi import MetodoOrdenamiento

class InsertionSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        for i in range(1, len(arr)):  # Big O: O(n)
            key = arr[i]  # Big O: O(1)
            j = i - 1  # Big O: O(1)
            while j >= 0 and getattr(key, columna) < getattr(arr[j],
                                                             columna):  # En el peor caso, este bucle recorre desde j hasta 0, por lo tanto, tiene una complejidad de O(j)
                arr[j + 1] = arr[j]  # Big O: O(1)
                j -= 1  # Big O: O(1)
            arr[j + 1] = key  # Big O: O(1)
        return arr

# Resumen del Big O:
# Tiempo de ejecución: O(n^2) en el peor caso y en el mejor caso.
# Espacio de memoria: O(1)
