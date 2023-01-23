# Explanation 3

## Rationale
For the "Rearrange Array Elements" problem, I implemented my own max binary heap data structure for the purposes of sorting the input array. With the input sorted, returning the maximal two numbers who's respective digits are composed by the numbers present in the input array is simple. 

## Runtime Analysis
The runtime complexity of this solution is `O(n log n)` and it's space complexity is `O(n)` where n is the length of the input array. The time complexity is achieved by sorting the input array via a max binary heap which guarantees constant time access to the max value in the heap by maintaining the heap invariant on `push` and `pop`. Memory utilization scales linearly with with the input length as we maintain a copy of the input throughout execution.