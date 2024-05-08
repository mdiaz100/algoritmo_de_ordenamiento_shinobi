from AlgoritmodO.Back_shi import MetodoOrdenamiento

class QuickSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        if len(arr) <= 1:  # O(1)
            return arr
        pivot = getattr(arr[len(arr) // 2], columna)  # O(1)
        left = [x for x in arr if getattr(x, columna) < pivot]  # O(n)
        middle = [x for x in arr if getattr(x, columna) == pivot]  # O(n)
        right = [x for x in arr if getattr(x, columna) > pivot]  # O(n)
        return QuickSort.sort(left, columna) + middle + QuickSort.sort(right, columna)  # O(log n)

#Resumen:

#Tiempo de ejecución: O(n log n) en el mejor caso, O(n^2) en el peor caso.
#Espacio de memoria: O(n) en el peor caso



