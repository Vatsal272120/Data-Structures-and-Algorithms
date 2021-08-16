/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. */

const twoNumberSumOptimized = (array, target) => {
  const hashTable = {};

  for (const i of array) {
    const potentialMatch = target - i;
    if (potentialMatch in hashTable) {
      return [potentialMatch, i];
    } else {
      hashTable[i] = true;
    }
  }

  return [];
};

const test1 = twoNumberSumOptimized([3, 5, -4, 8, 11, 1, -1, 6], 10);
console.log(test1);
