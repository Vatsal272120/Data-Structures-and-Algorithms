/* 
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

*/

const sortedSquaredArray = (array) => {
  sortedArray = new Array(array.length).fill(0);

  let smallerValueIdx = 0;
  let largerValueIdx = array.length - 1;

  for (let idx = array.length - 1; idx >= 0; idx--) {
    smallerValue = array[smallerValueIdx];
    largerValue = array[largerValueIdx];

    if (Math.abs(smallerValue) > Math.abs(largerValue)) {
      sortedArray[idx] = smallerValue * smallerValue;
      smallerValueIdx += 1;
    } else {
      sortedArray[idx] = largerValue * largerValue;
      largerValueIdx -= 1;
    }
  }

  return sortedArray;
};

const test = sortedSquaredArray([-5, -4, -3, -2, -1]);
console.log(test);
