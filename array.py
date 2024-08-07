def maxSubarraySum(arr,n):
    curr_sum=0
    max_sum=arr[0]
    for i in range(len(arr)):
        if curr_sum<0:
           curr_sum=0
        curr_sum+=arr[i]
        max_sum=max(max_sum,curr_sum)
    if max_sum<0:
        return 0
    return max_sum
    