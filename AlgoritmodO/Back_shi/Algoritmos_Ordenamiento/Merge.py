from AlgoritmodO.Back_shi import MetodoOrdenamiento
import pandas as pd

class MergeSort(MetodoOrdenamiento.MetodoOrdenamiento):

    @staticmethod
    def merge(arr1, arr2):
        i = 0  # O(1) 
        j = 0  # O(1) 
        result = []  # O(1) 
        while i < len(arr1) and j < len(arr2):  # O(n) 
            if arr2[j] > arr1[i]:  # O(1) 
                result.append(arr1[i])  # O(1) 
                i += 1  # O(1) 
            else:
                result.append(arr2[j])  # O(1) 
                j += 1  # O(1) 
        while i < len(arr1):  # O(n)
            result.append(arr1[i])  # O(1) 
            i += 1  # O(1) 
        while j < len(arr2):  # O(n) 
            result.append(arr2[j])  # O(1) 
            j += 1  # O(1) 

        return result  # O(1) 

    @staticmethod
    def sort(arr):
        if isinstance(arr, list):  # O(1)
            arr = pd.Series(arr)  # O(n) 

        if len(arr) <= 1:  # O(1) 
            return arr.values.tolist()  # O(1) 

        mid = len(arr) // 2  # O(1)
        left = MergeSort.sort(arr[:mid])  
        right = MergeSort.sort(arr[mid:])  

        return MergeSort.merge(left, right)  # O(n)

# Resumen del Big O:
# Tiempo de ejecución: O(n log n) en el peor caso y en el mejor caso.
# Espacio de memoria: O(n) en el peor caso y O(log n) en el mejor caso

