def contiguous_sum(num):
    size = len(num)
    max_sum_so_far = 0 
    max_ending_here = 0 

    for i in range(size):
        max_ending_here = max_ending_here + num[i]

        if max_ending_here < 0:
            max_ending_here = 0 

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far
