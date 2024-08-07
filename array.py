def max_subarray_sum(arr):
    max1=arr[0]
    max2=arr[0]

    for i in range(1,len(arr)):
        max2=max(arr[i],max2+arr[i])
        max1=max(max(max1,max2))

    return max1;
arr=[1,2,3,4,5]
print(max_subarray_sum)