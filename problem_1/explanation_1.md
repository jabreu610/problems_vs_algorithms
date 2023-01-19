# Explanation 1

## Rationale
For the "Finding the Square Root of an Integer" problem, the solution for every valid input lies within the range of all natural numbers between zero and the input, I leveraged binary search to find the floored square root of a provided integer. 

## Runtime Analysis
The runtime complexity of this solution is `O(log n)` where `n` is the range of natural numbers between zero and the input value, its space complexity is `O(1)` as memory utilization remains constant regardless of input in the worst case.