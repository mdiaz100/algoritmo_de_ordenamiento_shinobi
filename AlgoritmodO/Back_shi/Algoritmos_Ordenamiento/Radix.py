from AlgoritmodO.Back_shi import MetodoOrdenamiento

class RadixSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        def counting_sort(arr, exp):
            n = len(arr)   #O(1) 
            output = [0] * n   #O(1) 
            count = [0] * 10   #O(1) 

            for i in range(n):   #O(n) 
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):   #O(1)
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:  #O(n)
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(n):  #O(n)
                arr[i] = output[i]

        max_value = max(arr)   #O(n)
        exp = 1
        while max_value // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

        return arr
    
#Resumen:

#Tiempo de ejecución: O(n * d) en el peor caso, donde n es el tamaño de la entrada y d es el número de dígitos en el número más grande.
#Espacio de memoria: O(n) en el peor caso.