from AlgoritmodO.Back_shi import MetodoOrdenamiento

class RadixSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        @staticmethod
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = int(getattr(arr[i], columna) // exp)  # Convertir el índice a entero
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = int(getattr(arr[i], columna) // exp)  # Convertir el índice a entero
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        max_value = max(arr, key=lambda x: getattr(x, columna))  # O(n)
        exp = 1
        while getattr(max_value, columna) // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

        return arr

#Resumen:

#Tiempo de ejecución: O(n * d) en el peor caso, donde n es el tamaño de la entrada y d es el número de dígitos en el número más grande.
#Espacio de memoria: O(n) en el peor caso.