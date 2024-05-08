from AlgoritmodO.Back_shi.Algoritmos_Ordenamiento import Bubble,  Bucket, Counting, Heap, Insertion, Merge, Quick, Radix, Selection


class Creator:
    def __init__(self):
        self.dict_clases = {
            1: Merge.MergeSort(),
            2: Heap.HeapSort(),
            3: Radix.RadixSort(),
            4: Selection.SelectionSort(),
            5: Bubble.BubbleSort(),
            6: Counting.CountingSort(),
            7: Insertion.InsertionSort(),
            8: Quick.QuickSort(),
            9: Bucket.BucketSort()
        }

    def ordenar(self, num, arr, columna):
        metodo_nombres = {
            1: "Merge",
            2: "Heap",
            3: "Radix",
            4: "Selection",
            5: "Bubble",
            6: "Counting",
            7: "Insertion",
            8: "Quick",
            9: "Bucket"
        }
        clase = self.dict_clases.get(num)
        if clase:
            array_ordenado = clase.sort(arr, columna)
            return array_ordenado
        else:
            print("Número de método de ordenamiento no válido")
