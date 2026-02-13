def main_sort(number_list):
    mid=len(number_list)//2
    if len(number_list)<=1:
        return number_list
    low_list=main_sort(number_list[:mid])
    high_list=main_sort(number_list[mid:])
    return sorted_list(low_list,high_list)
def sorted_list(low_list,high_list):
    sorted_list_new_one=[]
    i=j=0
    while i<len(low_list)and j<len(high_list):
        if low_list[i]<high_list[j]:
            sorted_list_new_one.append(low_list[i])
            i+=1
        else:
            sorted_list_new_one.append(high_list[j])
            j+=1
    while i<len(low_list):
        sorted_list_new_one.append(low_list[i])
        i+=1
    while j<len(high_list):
        sorted_list_new_one.append(high_list[j])
        j+=1
    return sorted_list_new_one

n=input()
list_a=n.split()
number_list=list(map(int,list_a))
output=main_sort(number_list)
print(output)
