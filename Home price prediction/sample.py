# list = {1,2,3,4,5,5,7,8}

# arr = [1, 2, 3, 4, 5, 5, 7, 8]
# print(arr.index(5))
#
# arr.sort(reverse=True)
# lenth = len(arr)
# num = 5
#
#
# print(lenth - arr.index(5) - 1


# arr1[]={1,2,3,4,5,6,7,8,8,9,8} and arr2[]={2,3,1,0,9,7,5} 

arr1 = [1,2,3,4,5,6,7,8,8,9,8]
arr2 = [2,3,1,0,9,7,5]

count_arr = []
for ele1 in arr1:
    if ele1 not in arr2:
        count_arr.append(ele1)
print(count_arr)