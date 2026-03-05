def shell_sort(a):   # a = array
    n = len(a)

    gap = n // 2
    while gap > 0:
        # a "gapped" insertion sort for this gap size
        for i in range(gap, n):
            # Current element is placed in correct place
            temp = a[i]
            j = i

            # Shift earlier elements that are greater than temp
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap

            
            #place temp in its correct position
            a[j] = temp


        # reduce the gap
        gap //= 2


def print_a(a):
    print(" ".join(map(str, a)))

if __name__ == "__main__":
    a = [12,34,54,2,3]

    shell_sort(a)
    print_a(a)