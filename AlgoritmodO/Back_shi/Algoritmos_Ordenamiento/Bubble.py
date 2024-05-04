from AlgoritmodO.Back_shi import MetodoOrdenamiento


class BubbleSort(MetodoOrdenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
