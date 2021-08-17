""" Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 """

def sortedSquaredArray(array):
   sortedArray = [0 for _ in array]
   smallerIdx = 0
   largerIdx = len(array) - 1

   for idx in reversed(range(len(array))):

       smallerValue = array[smallerIdx]
       largerValue = array[largerIdx]

       if abs(smallerValue) > abs(largerValue):
           sortedArray[idx] = smallerValue * smallerValue
           smallerIdx +=1

       else:
           sortedArray[idx] = largerValue * largerValue
           largerIdx -=1


   return sortedArray            




    





s = sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])

print(s)