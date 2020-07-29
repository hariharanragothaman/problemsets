import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # cost is the array of flavor costs of icecream
    # money - the total amount of money they have
    print("Entering function logic")
    left = 0 
    right = len(cost)-1
    while left < right:
        sum1 = cost[left] + cost[right]
        if sum1 == money:
            print(left+1, right+1)
            break
        elif sum1 < money:
            left += 1
        else:
            right -=1

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        print("The cost is:", cost)
        print("Calling whatFlavor")
        whatFlavors(cost, money)
        print("After calling whatFlavor")
