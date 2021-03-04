n = 234


def SubtractProductandSum(n):
    sum_result = 0 
    product_result = 1 

    elements = [int(d) for d in str(n)]
    sum_result = sum(elements)
    for ele in elements:
        product_result = product_result * ele
    return (product_result - sum_result)

result = SubtractProductandSum(n)
print(result)
