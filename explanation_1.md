Analysis:
Time Complexity:
The time complexity is O(log(n)). Refer Design Choices section.

Space Complexity:
The space complexity is O(1). No additional space is required to execute this algorithm.

Design Choices:
I chose to alternate between finding upper and lower bounds in once iteration.
This makes it slightly more efficient than finding first the upper bound in one loop and lower bound in another loop.
This generally saves at least one iteration. 
I update the midpoint after calculating the upper and lower bounds. 
Then based on the value of the upper bound compared to the delta, I scale accordingly.
In this case, It may reduce the upper bound by more than half in each of the first few steps saving unnecessary iterations.
Once the delta gets to 0 or 1, then the answer is returned.