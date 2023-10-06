import random as rnd
import timeit, os

def main():
    def BS(data):
        for i in range(num):
            for j in range(num - i - 1):
                if data[j] > data[j+1]:
                    (data[j], data[j+1]) = (data[j+1], data[j])
                    
    def MSalg(data):
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            L = [0] * (n1)
            R = [0] * (n2)

            for i in range(0, n1):
                L[i] = arr[l + i]

            for j in range(0, n2):
                R[j] = arr[m + 1 + j]

            i = 0	
            j = 0	
            k = l	

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1


        def mergeSort(arr, l, r):
            if l < r:
                m = l+(r-l)//2
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)
                merge(arr, l, m, r)

        mergeSort(data, 0, num-1)

    def QS(data):
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1

            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])

            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)

        quickSort(data, 0, num - 1)

    num = int(input('Enter the number of elements: '))
    arr = rng = []

    bstc = mstc = qstc = 0

    arr = rnd.sample(range(1, num * 10 + 1), num)
    rnd.shuffle(arr)

    for i in range(num):
        rng.append(i+1)
    
    f = open(os.path.dirname(__file__) + '\generated_array.txt', 'a+')
    f.writelines(str(arr))
    f.write('\n')
    f.close()
    
    bstc = timeit.timeit(lambda: BS(arr.copy()), number=1)
    mstc = timeit.timeit(lambda: MSalg(arr.copy()), number=1)
    qstc = timeit.timeit(lambda: QS(arr.copy()), number=1)

    return bstc, mstc, qstc