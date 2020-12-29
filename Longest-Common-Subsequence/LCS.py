# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:19:54 2020

@author: Iman Irajian (iman.irajian@gmail.com)
"""

import numpy as np
    
def LCS(X, Y):   
      
    def Print_LCS(i, j):
        if i==0 or j==0:
            return
        elif b[i, j] == UL:
            Print_LCS(i-1, j-1)
            print( X[i-1], end="" )
        elif b[i, j] == U:
            Print_LCS(i-1, j)
        else:
            Print_LCS(i, j-1)
                        
    UL = 3 # up-left
    U = 2  # up
    L = 1  # left

    print("X:", "\t"*3, X)
    print("Y:", "\t"*3, Y)
    
    m = len(X)
    n = len(Y)
    
    # the path matrix "b" is actually (m x n)
    # (m+1 x n+1) makes indexing similar to pseudo-code    
    b = np.zeros( (m+1, n+1), dtype=int )
    c = np.zeros( (m+1, n+1), dtype=int )        
            
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1] :
                c[i, j] = c[i-1, j-1] + 1
                b[i, j] = UL
            elif b[i-1, j] >= b[i, j-1]:
                c[i, j] = c[i-1, j] 
                b[i, j] = U
            else:
                c[i, j] = c[i, j-1]
                b[i, j] = L
    
    if c[m, n] > 0:
        print("LCS (" + str(c[m, n]) + "):\t ", end="")
        Print_LCS(m, n)
    else:
        print("No LCS", end="")
    print("\n")


LCS('AB', 'T')

LCS('AB', 'B')

LCS('ABCBDAB', 'BDCABA')

LCS('ACCGGTCGAGT', 'GTCGTTC')

LCS('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA,', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA')