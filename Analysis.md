Ayush kumar
Unscramble Computer Science Problems

Task0
Time Complexity: O(1)
Description: Input does not affects run time

Task 1:
The run-time is O(n x m) where n is the length of the input csv and m is the length of the unique_telephone_list. 
The main work for the run-time analysis is done in parse_telephone_data(csv) and add_telephone_number_to_list. 
There are technically two for loops executed, 
but the constant would be dropped as well as any additional constants for 
the code in the other methods (count_unique_telephone_numbers and add_telephone_number_to_list).


Task2:

This task has 2 for loops, taking 1 list as input, populating a dictionary with the
elements of a list, of which one value of the dictionary is calculated in the
for loop. In the second for loop, 1 iteration through the dictionary returns
the value with the highest value - so: 0(n) + 0(n) = 0(2n). With increasing input,
the time complexity will be 0(n).

Task3:

Here we have 2 for loops, as well as a sorted() statement on line 67,
which brings the time complexity to 0(n logn).


Task4:
Time Complexity: O(n+nlogn)
Description: For loop and python sort
