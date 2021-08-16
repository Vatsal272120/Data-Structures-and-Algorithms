"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 """
 # O(n) Time |  O(n) Space  n = length of input array
def twoNumberSumOptimized(array, target) :
   hashTable = {} 

   for num in array: 
       potentialMatch = target - num

       if potentialMatch in hashTable: 
           return [potentialMatch, num]
           
       hashTable[num] = True

 



# Optimized 
test1= twoNumberSumOptimized([3, 5, -4, 8, 11, 1, -1, 6], 10)
test2 = twoNumberSumOptimized([4, 6],10)



print(test1, test2)