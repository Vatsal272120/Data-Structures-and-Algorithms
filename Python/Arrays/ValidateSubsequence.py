""" Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not). """


"""  O(n) Time | O(1) space """
def isValidSubsequenceOne(array, sequence) :
    seqIdx = 0
    arrayIdx = 0

    while arrayIdx < len(array) and seqIdx < len(sequence) :
        if array[arrayIdx] == sequence[seqIdx]:
            # seqIdx will only increase if match is found
            seqIdx += 1 
        # arrayIdx will be incremented by 1 regardless if match is found
        arrayIdx +=1

    return seqIdx == len(sequence)

    

"""  O(n) Time | O(1) space """
def isValidSubsequenceTwo(array, sequence) :
    seqIdx = 0

    for value in array : 
        if seqIdx == len(sequence) :
            break
        if sequence[seqIdx] == value :
            seqIdx += 1

    return seqIdx == len(sequence)


s = isValidSubsequenceOne([5, 1, 22, 25, 6, -1, 8, 10],  [1, 6, -1, 10])
s1 = isValidSubsequenceTwo([5, 1, 22, 25, 6, -1, 8, 10],  [1, 6, -1, 10])


print(s,s1)