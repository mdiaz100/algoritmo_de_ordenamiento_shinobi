from AlgoritmodO.Back_shi import MetodoOrdenamiento

class CountingSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        max_value = max(arr)  # Big O: O(n)
        min_value = min(arr)  # Big O: O(n)
        count = [0] * (max_value - min_value + 1)  # Big O: O(k), donde k es el rango de valores en el arreglo

        for num in arr:
            count[num - min_value] += 1  # Big O: O(1)

        sorted_arr = []
        for i in range(len(count)):  # Big O: O(k)
            sorted_arr.extend([i + min_value] * count[i])  # Big O: O(n)

        return sorted_arr

# Resumen del Big O:
# Tiempo de ejecución: O(n + k), donde n es el tamaño del arreglo y k es el rango de valores en el arreglo.
# Espacio de memoria: O(n + k)
