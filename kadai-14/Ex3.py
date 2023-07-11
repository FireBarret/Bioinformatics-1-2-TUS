# coding: UTF-8
import math
import sys

seq_A="ATGCATCC"
seq_B="AGGCATCC"

#ここからプログラムを書いてください
def discordance(seq1, seq2):
    dis = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dis += 1
    return dis

def P_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        print("配列長は異なります")
        sys.exit()
    dis = discordance(seq1, seq2)
    return dis/max(len(seq1),len(seq2))
def Poisson_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        print("配列長は異なります")
        sys.exit() 
    dis = discordance(seq1, seq2)
    return -math.log(1-dis/max(len(seq1),len(seq2)))
    

print(P_distance(seq_A, seq_B))