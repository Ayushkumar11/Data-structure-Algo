Analysis:
Time Complexity:
The time complexity is split into there for insert, find and suffixes. Refer Design Choices section.

Space Complexity:
The space complexity is split into there for insert, find and suffixes. Refer Design Choices section.

Design Choices:
I used a Trie with DFS In-order search. 
This was tricky, but the best way to approach this problem since,
we had to traverse all the nodes for a given input prefix to find all the suffixes related to it.
Time complexity for insert and find is O(n) to loop through each char in word. 
Space complexity for insert and find is O(mn) where m is the word inserting/finding and n is the total number of words.

Time complexity for suffixes is O(V + E) where V is the vertices and E is the edges.
In theory, each branch could be traversed.
Space complexity for suffixes is O(bm) where b is the branches to travel and m is the longest word.