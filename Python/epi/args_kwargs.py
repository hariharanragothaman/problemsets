def foo(u, v, *args):
    print('u,v = ' + str((u,v)))
    for i in range(len(args)):
        print ('args {0} = {1}'.format(str(i), str(args[i])))

# Example of kwargs


def foo_new(u, v, *args, **kwargs):
    print('u,v = ' + str((u,v)))
    for i in range(len(args)):
        print ('args {0} = {1}'.format(str(i), str(args[i])))
    for key, value in kwargs.items():
        print('keyword, value = ' + str((keyword, value)))

if __name__ == '__main__':
    foo(1, 'euler', 2.71, [6,28])
    foo_new(1, 'euler', (2.71, [6,28]), {'name':'cfg', 'rank':1})
