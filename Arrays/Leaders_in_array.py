"""
Leaders in an array

Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.
===========================
Example 1 :
Input: n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
===========================
Example 2 :
Input:n = 5
A[] = {1,2,3,4,0}
Output: 4 0
============================
Transverse through array from last element to first by taking last element as maximum first and append all the maximums that you encounter along the way
    Time complexity  = O(N)
    Space complexity = O(1)
"""
## Solution ##
def leaders(A, N):
    ans = []
    ans.append(A[-1])
    maxi = A[-1]
    for i in range(N-1):
        if A[N-i-2] >= maxi:
            maxi = A[N-i-2]
            ans.append(maxi)
        else:
            continue
    ans.sort(reverse=True)
    return ans
print(leaders([1, 2, 3, 4, 0], 5)
      
 
