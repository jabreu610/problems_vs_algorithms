# Explanation 5
I do not believe the project description provided enough guidance for the student to determine what part of the notebook they should analyze here, I opted to focus on the `TrieNode`'s `suffixes` method as that is the main functionality tested by the notebook. If additional details are required please update [the page](https://learn.udacity.com/nanodegrees/nd256/parts/cd1887/lessons/032713d7-07e0-468f-8393-7b34bf2899e7/concepts/c7047d0a-e63f-47b3-bb45-82b75b00c701) for this project as responding to code reviews for poorly documented project requirements is an egregious waste of student time and money.

## Rationale
For the "Autocomplete with Tries" problem, I chose to utilize Python's `defaultdict` class to simplify inserting new words into our `Trie`. The `TrieNode`'s `suffixes` method leverages depth first search via recursion to produce a list of all valid suffixes from the inital TrieNode.

## Runtime Analysis
The runtime and space complexity of the `TrieNode`'s `suffixes` method is `O(n)` where `n` represents the total number of nodes defined under the sub-tree rooted by the prefix `TrieNode`. Its runtime scales linearly with the total number nodes under the chosen prefix as we visit each node to build our list of suffixes. Its memory utilization scales linearly with the maximum depth of the sub-tree rooted by the prefix, it is said to scale linearly with the number of nodes in the worst case given a subtree where every node has a single child.

### Additional Notes after 1st Review
As mentioned at the head of this document, I believe this prompt was lacking detail on what to focus the explanation on. The reviewer insisted including runtime analysis for every component, that follows below:

1. `TrieNode` constructor - Runtime and space complexity of `O(1)`, the constructor for the `TrieNode` accepts no input.
2. `TrieNode` `suffixes` method - As mentioned in the Runtime Analysis section, has a runtime and space complexity of `O(n)` where `n` represents the total number of nodes defined under the sub-tree rooted by the prefix, see Runtime Analysis for more detail
3. `Trie` constructor - Runtime and space complexity of `O(1)`, the constructor for the `Trie` accepts no input.
4. `Trie` `insert` method - Runtime and space complexity of `O(n)` where `n` represents the character length of the word passed as input. In the worst case, new nodes are created per letter not already present in the Trie via a common prefix
5. `Trie` `find` method - Runtime complexity of `O(n)` where `n` represents the character length of the input prefix. It has a space complexity of `O(1)` as memory allocation during runtime does not scale with the input.
