trib = {}
def count_possibilities(n):
    try:
        return trib[n]
    except KeyError:
        if(n == 0):
            return 1
        elif(n < 3):
            return n
        else:
            val = count_possibilities(n-1) + count_possibilities(n-2) + count_possibilities(n-3)
            trib[n] = val
            return val

print(count_possibilities(6))



"""

https://www.reddit.com/r/adventofcode/comments/kapbjb/year_2020_day_10_part_2_additional_examples_for/





In the sample set (make sure you include 0, 22 doesn't matter for part 2) you have:

0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19
Calculating the differences:

1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3
So we have 4 things to multiply together (each run of 1s). If there's only one 1, that means only one way through:

0, 1, 4

You can only get to 4 by going through 1, and that has to come from 0.

4, 5, 6, 7
You have 4 ways to go through this block. 4 -> 7, 4 -> 5 -> 7, 4 -> 5 -> 6 -> 7, 4 -> 6 -> 7.

10, 11, 12
There are 2 ways through this one. 10->11->12, 10->12.

So in the end you have to multiply 1*4*2*1 together, which gives us 8. If the runs were longer we'd have to continue the calculations. For a 4-run of 1s, there are 7 routes through.

"""
