from AlgoritmodO.Back_shi import MetodoOrdenamiento

class BucketSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr, columna):
        max_value = getattr(max(arr, key=lambda x: getattr(x, columna)), columna)
        min_value = getattr(min(arr, key=lambda x: getattr(x, columna)), columna)
        bucket_range = (max_value - min_value) / len(arr)
        buckets = [[] for _ in range(len(arr) + 1)]

        for num in arr:
            valor_columna = getattr(num, columna)
            index = int((valor_columna - min_value) / bucket_range)
            if index == len(arr):
                index -= 1
            buckets[index].append(num)

        for i in range(len(arr)):
            buckets[i].sort(key=lambda x: getattr(x, columna))

        k = 0
        for i in range(len(arr)):
            for j in range(len(buckets[i])):
                arr[k] = buckets[i][j]
                k += 1
        return arr

# Resumen del Big O:
# Tiempo de ejecución: O(n^2) en el peor caso, O(n * log(n)) en el mejor caso.
# Espacio de memoria: O(n)
