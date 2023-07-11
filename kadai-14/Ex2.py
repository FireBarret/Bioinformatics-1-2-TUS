# coding: UTF-8

seq_A="TGACTGATCGTATC"
seq_B="TGCAGTCGATGTAC"

#ここからプログラムを書いてください
def discordance(seq1, seq2):
    dis = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dis += 1
    return dis
def P_distance(seq1, seq2):
    dis = discordance(seq1, seq2)
    return round(dis/max(len(seq1),len(seq2)),3)
print(P_distance(seq_A, seq_B))