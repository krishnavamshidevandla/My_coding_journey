"""
Search in a rotated Array

Given a sorted and rotated array A of N distinct elements which is rotated at some point, 
and given an element key. The task is to find the index of the given element key in the array A. 
The whole array A is given as the range to search.

===========================
Example 1 :
Input: N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
l = 0 , h = 8
Output: 5
===========================
Example 2 :
Input: N = 4
A[] = {3, 5, 1, 2}
key = 6
l = 0 , h = 3
Output: -1
============================
As the required complexity is same as the binary search lets try to mimic the same structure of binary search. Create a while loop or use recursion till left <= right
assign a mid value i.e. left+right /2. Check if it is the answer. If not continue to check if mid => left if true left array is sorted then check whether key is 
between the left and mid if there change the parameters accordingly else check in the other half of the array. If mid ! >= left the right array is sorted repeat the
same.

    Time complexity  = O(LogN)
    Space complexity = O(1)

"""
## Solution ##

def search(A, l, h, key):
  while l <= h:
      mid = (l+h)//2
      if A[mid] == key:
          return mid
      if A[l] <= A[mid]:
          if key >= A[l] and key < A[mid]:
              h = mid -1
          else:
              l = mid +1
      else:
          if key <= A[h] and key > A[mid]:
              l = mid +1
          else:
              h = mid -1
  return -1
