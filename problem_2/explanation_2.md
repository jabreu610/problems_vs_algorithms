# Explanation 2

## Rationale
For the "Search in Rotated Sorted Array" problem, I leverage binary search to both identify the pivot index the ordered array is rotated on and to find the target in the sorted array if present.

## Runtime Analysis
The runtime complexity of this solution is `O(log n)` when `n` is the length of the input array, it's space complexity is `O(n)` as we temporarily store a sorted copy of the input array for resolving the index of the target value via binary search.