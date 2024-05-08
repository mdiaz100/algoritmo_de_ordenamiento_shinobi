from AlgoritmodO.Back_shi import MetodoOrdenamiento


class SelectionSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        n = len(arr)  # O(1)
        for i in range(n):  # O(n)
            min_idx = i  # O(1)
            for j in range(i + 1, n):  # O(n)
                if getattr(arr[j], columna) < getattr(arr[min_idx], columna):  # O(1)
                    min_idx = j  # O(1)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # O(1)
        return arr

#Resumen:

#Tiempo de ejecución: O(n^2) en el peor caso.
#Espacio de memoria: O(1) - El algoritmo utiliza espacio constante adicional para variables temporales.