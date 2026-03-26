def insertion_sort (arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >=0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[0]
    menores = [x for x in arr[1:] if x <= pivo]
    maiores = [x for x in arr[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)
