def bubble_sort (A : list) -> list:
    for i in range(len(A)):
        swamp_flag = False
        for j in range(len(A)-1):
            if (A[j] > A[j+1]):
                swamp_flag = True
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        if swamp_flag is False:
            return A
    return A
x: int = 15
Lista_Bubble : list =[i for i in range(1, 100000, 15)]
print(bubble_sort(Lista_Bubble))

#2

def bubble_sort (A : list) -> list:
    for i in range(len(A)):
        for j in range(len(A) -i -1):
            if (A[j] > A[j+1]):
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A
x: int = 15
Lista_Bubble : list =[i for i in range(1, 100000, 15)]
print(bubble_sort(Lista_Bubble))