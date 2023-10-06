import matplotlib.pyplot as plt
import random as rnd
import time
import os
import time_complexity_sorting_algo as tcsa

plt.rcParams["figure.figsize"] = (10,6)

def bubble_sort(lst, n, x):
    if sorting_algo != 4:
        n = int(input('Enter the number of elements:'))
        lst = []
        x = []
        if input_type == 1:
            for i in range(n):
                lst.append(int(input(f'Element {i+1}: ')))
                x.append(i+1)
        else:
            lst = rnd.sample(range(1, n * 10 + 1), n)
            rnd.shuffle(lst)
            for i in range(n):
                x.append(i+1)

    print('Before Sorting:', lst)
    start = time.time()
    for i in range(n):
        for j in range(n - i - 1):
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            bars = plt.bar(x, lst)
            bars[j].set_color('red')
            plt.text(j, lst[j], lst[j])
            plt.pause(0.00001)
            plt.clf()
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    end = time.time()
    print('After Sorting:', lst)

    bubble_sort_time_complexity = end-start
    plt.xlabel('No. of elements')
    plt.ylabel('Range of elements')
    plt.text(0.3, 100, bubble_sort_time_complexity)
    plt.bar(x, lst)
plt.show()


def merge_sort(lst, n, x, b):
    def merge(a, l, m, u):
        i = l
        j = m+1
        k = l
        while i <= m and j <= u:
            if a[i] <= a[j]:
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
            k += 1
        if i > m:
            while j <= u:
                b[k] = a[j]
                j += 1
                k += 1
        else:
            while i <= m:
                b[k] = a[i]
                i += 1
                k += 1

        for k in range(l, u+1):
            a[k] = b[k]

    def MS(a, l, u):
        if l < u:
            m = (l+u) // 2
            MS(a, l, m)
            MS(a, m+1, u)
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            plt.text(l, a[l], a[l])
            plt.bar(x, a)
            plt.bar(x[l:m+1], a[l:m+1], color='red')
            plt.bar(x[m+1:u+1], a[m+1:u+1], color='green')
            plt.pause(0.00001)
            plt.clf()
            merge(a, l, m, u)
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            plt.text(l, a[l], a[l])
            plt.bar(x, a)
            plt.pause(0.00001)
            plt.clf()

    if sorting_algo != 4:
        n = int(input("Enter the number of elements: "))
        b = [0] * n
        x = []
        lst = []
        if input_type == 1:
            for i in range(n):
                lst.append(int(input(f'Element {i+1}: ')))
                x.append(i+1)
        else:
            lst = rnd.sample(range(1, n * 10 + 1), n)
            rnd.shuffle(lst)
            for i in range(n):
                x.append(i+1)

    print("Before sorting:", lst)
    start = time.time()
    MS(lst, 0, n-1)
    end = time.time()
    merge_sort_time_complexity = end-start
    print("After sorting:", lst)
    plt.xlabel('No. of elements')
    plt.ylabel('Range of elements')
    plt.text(0.3, 100, merge_sort_time_complexity)
    plt.bar(x, lst)
plt.show()


def quick_sort(lst, n, x):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            plt.xlabel('No. of elements')
            plt.ylabel('Range of elements')
            bars = plt.bar(x, lst, color='lightblue')
            plt.bar(x[low:j+1], array[low:j+1], color='red')
            plt.bar(x[j+1:j+2], array[j+1:j+2], color='orange')
            plt.bar(x[j+2:high+1], array[j+2:high+1], color='green')
            plt.pause(0.00001)
            plt.clf()
            if array[j] <= pivot:
                i = i + 1
                bars[i].set_color('orange')
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        bars = plt.bar(x, lst, color='lightblue')
        plt.pause(0.00001)
        plt.clf()

        return i + 1


    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quickSort(array, low, pi - 1)
            quickSort(array, pi + 1, high)


    if sorting_algo != 4:
        n = int(input('Enter number of elements: '))
        x = []
        lst = []
        if input_type == 1:
            for i in range(n):
                lst.append(int(input(f'Element {i+1}: ')))
                x.append(i+1)
        else:
            lst = rnd.sample(range(1, n * 10 + 1), n)
            rnd.shuffle(lst)
            for i in range(n):
                x.append(i+1)

    print("Before sorting:", lst)

    size = len(lst)
    start = time.time()
    quickSort(lst, 0, size - 1)
    end = time.time()
    print("After sorting:", lst)

    quick_sort_time_complexity = end-start
    plt.xlabel('No. of elements')
    plt.ylabel('Range of elements')
    plt.text(0.3, 100, quick_sort_time_complexity)
    plt.bar(x, lst)
plt.show()

try:
    sorting_algo = 0
    bubble_sort_time_complexity = 0
    merge_sort_time_complexity = 0
    quick_sort_time_complexity = 0

    while sorting_algo != 5:
        print('\nAlgorithm to visualize:')
        print('1. Bubble Sort')
        print('2. Merge Sort')
        print('3. Quick Sort')
        print('4. Compare time complexities')
        print('5. Quit')
        sorting_algo = int(input('Choice:'))

        if sorting_algo == 4:
            time1, time2, time3 = tcsa.main()
            print(f'Bubble Sort: {time1} sec\nMerge Sort: {time2} sec\nQuick Sort: {time3} sec')
            continue
        elif sorting_algo == 5:
            break

        print('How do you want to generate your input?')
        print('1. Manual Entry\n2. Randomly generated array')
        input_type = int(input('Choice:'))

        if sorting_algo == 1:
            bubble_sort([], 0, [])
        elif sorting_algo == 2:
            merge_sort([], 0, [], [])
        elif sorting_algo == 3:
            quick_sort([], 0, [])

        plt.pause(3)
        plt.close()
finally:
    os.remove(os.path.dirname(__file__) + '\generated_array.txt')