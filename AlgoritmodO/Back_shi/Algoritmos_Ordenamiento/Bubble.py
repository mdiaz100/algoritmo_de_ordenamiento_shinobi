from AlgoritmodO.Back_shi import MetodoOrdenamiento

class BubbleSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        # Big O: O(n) - debido a la operación len(arr)
        n = len(arr)
        
        for i in range(n):
            # Big O: O(n) - debido a range(n)
            for j in range(0, n - i - 1):
                # Big O: O(1) - todas las operaciones dentro del bucle son de tiempo constante
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Big O: O(1) - devolver la lista ordenada no depende del tamaño de la lista
        return arr

# Resumen del Big O:
# Tiempo de ejecución: O(n^2) en el peor caso, O(n) en el mejor caso.
# Espacio de memoria: O(1)
