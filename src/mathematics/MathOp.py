import math
from scipy.stats import hypergeom


def choose(n, k):
    return math.comb(n, k)

def faculty(n):
    if n > 1:
        return n*faculty(n-1)
    else:
        return 1

def hypGemProb(k,N,K,n):
    prob = 0
    for i in range(k):
        prob = prob + hypergeom.pmf(i,N,K,n)
    return 1-prob


def frequency(lst):
    tot = sum(lst)
    frequency_lst = []
    for i in lst:
        freq = i/tot
        frequency_lst.append(freq)
    return frequency_lst