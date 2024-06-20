#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins

    def buy(self, req_items, money):

        if req_items > self.num_items:
            return "Not enough items in the machine"

        if (req_items * self.item_coins) > money:
            return "Not enough coins"
        else:
            self.num_items -= req_items
        return (money - (req_items * self.item_coins))

            
    pass
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(change)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            print(e)
            fptr.write(str(e) + "\n")


    fptr.close()