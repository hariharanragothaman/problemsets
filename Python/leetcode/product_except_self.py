ll = [0, 0, 0, 0]
print(ll)

l2 = [0]*len(ll)

for i in range(len(ll)):
    int_list = [data for k, data in enumerate(ll) if k!=i]
    print(int_list)

    # Finding the product
    prod = 1
    for elem in int_list:
        prod = prod * elem
    l2[i] = prod

print(l2)
