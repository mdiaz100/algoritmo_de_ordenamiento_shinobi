from AlgoritmodO.Back_shi import MetodoOrdenamiento
import pandas as pd


class MergeSort(MetodoOrdenamiento.MetodoOrdenamiento):

    @staticmethod
    def merge(arr1, arr2):
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr2[j] > arr1[i]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    @staticmethod
    def sort(arr):
        if isinstance(arr, list):
            arr = pd.Series(arr)  # Convertir la lista a una serie de Pandas

        if len(arr) <= 1:
            return arr.values.tolist()  # Convertir la serie de Pandas de nuevo a lista antes de retornarla

        mid = len(arr) // 2
        left = MergeSort.sort(arr[:mid])
        right = MergeSort.sort(arr[mid:])

        return MergeSort.merge(left, right)
