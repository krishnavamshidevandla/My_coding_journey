"""
Count inversion

Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
===========================
Example 1 :
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
===========================
Example 2 :
Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
============================
Divide the array into almost two equal halves and recurse the function with individual parts and sort each part by merge sort function.
While merging the two parts compare left and right sub arrays if i'th element of left array is greater than j'th element of right array then all elements from
i'th element should be greater than j'th element in right array. Continue the process till you reach the individual elements

    Time complexity  = O(NLogN)
    Space complexity = O(N)
"""
## Solution ##
def inversionCount(arr, N):
    count = 0
    if (len(arr)>1):
        m = (len(arr))//2
        l = arr[:m]
        r = arr[m:]
        count += inversionCount(l, len(l))
        count += inversionCount(r, len(r))  
        i=j=k=0
        while (i <len(l) and j < len(r)):
            if l[i] > r[j]:
                arr[k] = r[j]
                count += len(l) - i
                j += 1
            else:
                arr[k] = l[i]
                i += 1
            k +=1
        while i < len(l):
            arr[k] = l[i]
            k+=1
            i+=1
        while j < len(r):
            arr[k] = r[j]
            k+=1
            j+=1
    return count
print(inversionCount([2, 4, 1, 3, 5], 5))
