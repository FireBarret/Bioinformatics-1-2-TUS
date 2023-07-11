# coding: UTF-8
import math
import sys

seq_A="ATGCATCC"
seq_B="AGGCACC"

#ここからプログラムを書いてください
def accordance(seq1, seq2):
    dis = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            dis += 1
    return dis
def Poisson_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        print("配列長は異なります")
        sys.exit()
    dis = accordance(seq1, seq2)
    if dis ==  0:
        print("計算不可能")
        sys.exit()
    else:
        return round(-math.log(dis/max(len(seq1),len(seq2))),3)
    
print(Poisson_distance(seq_A, seq_B))