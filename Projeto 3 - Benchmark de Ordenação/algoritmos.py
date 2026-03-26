a = [9, 2, 4, 7, 6, 5]

def insertion_sort (arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >=0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = chave
    print(arr) 
        
insertion_sort (a)

#def quick_sort(arr):
