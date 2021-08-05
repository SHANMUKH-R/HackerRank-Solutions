# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:08:50 2021

@author: R.SHANMUKH
"""

#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine():
    def __init__(self,variable1,variable2):
        self.variable1=variable1
        self.variable2=variable2

    def buy(self,x,y):
        if(self.variable1>=x and x*self.variable2<=y):
            self.variable1-=x
            return y-(x*self.variable2)
        else:
            if(self.variable1<x):
                return "Not enough items in the machine"
            else:
                return "Not enough coins"
            
            
         
        
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
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
