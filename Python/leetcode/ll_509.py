def fib(self, N):
     """
    :type N: int
    :rtype: int
    """
    f_term = 0
    s_term = 1
    t_term = 0 
    i = 1
        
    if N == 0: return 0
    if N == 1: return 1
    else:
        while i < N:
            t_term = s_term + f_term
            f_term = s_term
            s_term = t_term
            i = i+1
    return t_term
