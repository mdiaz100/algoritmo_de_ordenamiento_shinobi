from AlgoritmodO.Back_shi import MetodoOrdenamiento

class BucketSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        max_value = max(arr)
        min_value = min(arr)
        bucket_range = (max_value - min_value) / len(arr)  # Big O: O(n)

        buckets = [[] for _ in range(len(arr) + 1)]  # Big O: O(n)

        for num in arr:
            index = int((num - min_value) / bucket_range)  # Big O: O(1)
            if index == len(arr):
                index -= 1
            buckets[index].append(num)  # Big O: O(1) (amortizado)

        for i in range(len(arr)):  # Big O: O(n)
            buckets[i].sort()  # Big O: O(n * log(n))

        k = 0
        for i in range(len(arr)):  # Big O: O(n)
            for j in range(len(buckets[i])):  # Big O: O(n)
                arr[k] = buckets[i][j]  # Big O: O(1)
                k += 1

        return arr

# Resumen del Big O:
# Tiempo de ejecución: O(n^2) en el peor caso, O(n * log(n)) en el mejor caso.
# Espacio de memoria: O(n)
