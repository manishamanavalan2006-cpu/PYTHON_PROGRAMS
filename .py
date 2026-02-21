def quick_sort(list_a):
    if len(list_a)<=1: #base case
        return list_a
    pivot=list_a[0]
    small_value=[i for i in list_a[1:] if i<=pivot]
    large_value=[j for j in list_a[1:] if j>=pivot]

    return quick_sort(small_value)+[pivot]+quick_sort(large_value)

toys=input()
list_split=input().split()
intergal_list=list(map(int,list_split))
output=quick_sort(intergal_list)
print(output)
