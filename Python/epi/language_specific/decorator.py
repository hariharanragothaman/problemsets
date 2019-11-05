import timeit

def time_function(f):
    begin = timeit.default_timer()
    result = f()
    end = timeit.default_timer()
    print ("Function call took " + str(end-begin) + " seconds to execute")

def foo():
    print("Entering foo function")

def ackerman(m,n):
    if m==0:
        return n+1
    elif n==0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1, ackerman(m,n-1))

#@time_function is equal to: foo=@time_function(foo)

def time_func(f):
   def wrapper(*args, **kwargs):
       begin = timeit.default_timer()
       result = f(*args, **kwargs)
       end = timeit.default_timer()
       print ('Function call with arguments {all_args} took '.format(all_args='\t'.join(str(args))) + str(end-begin) + ' seconds to execute.')
       return result

   return wrapper

@time_func
def foo_new():
    print ("Entering foo function")

if __name__ == '__main__':
    foo_new()
