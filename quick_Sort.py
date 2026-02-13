def quick_sort(list_a):
    if len(list_a) <= 1:  # base case
        return list_a

    pivot = list_a[0]
    small_value = [i for i in list_a[1:] if i <= pivot]
    large_value = [i for i in list_a[1:] if i > pivot]

    return quick_sort(small_value) + [pivot] + quick_sort(large_value)

# Input list as space-separated numbers
list_split = input("Enter numbers separated by space: ").split()
integer_list = list(map(int, list_split))

# Sorting
output = quick_sort(integer_list)
print("Sorted list:", output)
