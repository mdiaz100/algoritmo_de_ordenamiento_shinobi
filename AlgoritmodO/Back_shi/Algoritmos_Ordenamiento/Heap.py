from AlgoritmodO.Back_shi import MetodoOrdenamiento

class HeapSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and getattr(arr[left], columna) > getattr(arr[largest], columna):
                largest = left

            if right < n and getattr(arr[right], columna) > getattr(arr[largest], columna):
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):  # Big O: O(n)
            heapify(arr, n, i)  # Big O: O(log n)

        for i in range(n - 1, 0, -1):  # Big O: O(n)
            arr[i], arr[0] = arr[0], arr[i]  # Big O: O(1)
            heapify(arr, i, 0)  # Big O: O(log n)

        return arr

# Resumen del Big O:
# Tiempo de ejecución: O(n * log n)
# Espacio de memoria: O(1)
