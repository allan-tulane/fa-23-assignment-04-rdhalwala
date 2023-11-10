# CMPS 2200 Assignment 4
## Answers

**Name:**__Raiya Dhalwala_______________________


Place all written answers from `assignment-04.md` here for easier grading.
I tried...

1a) In the greedy algorithm, first go through the highest value coins. If N=0 then it returns 0 (base case). The value input will be subtracted by 2^k coin taken away while greater than 0. Once it hits 0 the result will be returned. 

1b)Greedy choice property: Choosing the largest denomination - power of 2 - that is not bigger than the remaining amount is optimized. Let there be an optimal solution where larger denomination is chosen. We can replace this choice with k^2 without increasing the total coins used. The larger denomination can be split without using additional coins, which shows optimality.
Don't understand optimal substructure

1c) The work and span are O(logn).

2a)
A counter example is coins = [1, 5, 7, 13, 14], N = 20. The algorithm would select 14, 5, and 1, return 3 coins. The optimal solution would return 2 coins.

2b)Don't understand optimal substructure

2c)
A dynamic approach would be to iterate through coins combinations and find the best one that has the least total coins used. The work would be O(n*coins) and span would be O(n).

