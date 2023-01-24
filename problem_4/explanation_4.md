# Explanation 4

## Rationale
For the "Dutch National Flag Problem", I iterate through the `input_list` exactly once as specified by the problem definition. Through this iteration I build up an sorted answer list.

## Runtime Analysis
The runtime complexity of this solution is `O(n)` and its space complexity is `O(n)` where n is the length of the unsorted input array. Runtime scales linearly with the input array's length as we iterate through the input once to build our result. Memory utilization also scales linearly with input length as we build the result list as a seperate array.