/* 

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not)

*/

// O(n) Time | O(1) space
const isValidSubsequenceOne = (array, seq) => {
  arrIdx = 0;
  seqIdx = 0;

  while (arrIdx < arr.length && seqIdx < seq.length) {
    if (array[arrIdx] === sequence[seqIdx]) {
      //seqIdx will only increase if match is found
      seqIdx++;
    }
    //arrayIdx will be incremented by 1 regardless if match is found
    arrIdx++;
  }

  return seqIdx === sequence.length;
};

// O(n) Time | O(1) space
const isValidSubsequenceTwo = (array, seq) => {
  seqIdx = 0;

  for (const value in array) {
      if (seqIdx === array.length) {
          
      }
  }
};
