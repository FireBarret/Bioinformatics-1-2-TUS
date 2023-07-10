f1 = 'ATGGCTATGATGGAGGTCCAGG'
r1 = 'TTAGCCAACTAAAAAGGCCCCAAAAAAACTGG'
r2 = 'TTATTTTGCGGCCCAGAGCCTTTTCATTCTTG'

def GCratio(seq):
    x = 0
    for i in range(0, len(seq)):
        if seq[i] == "G" or seq[i] == "C":
            x = x + 1
        else:
            x = x + 0
    GCper = round(x/len(seq)*100, 2)
    return GCper

def tmvalue(seq):
    Tm = round(81.5 + (16.6 * (-1.3)) + (0.41 * GCratio(seq)) - (500/len(seq)), 2)
    return Tm

def optimal_tm(seq):
    newseq = seq
    opt_val_list = []
    for nuc in range(12):
        print(str(nuc) , str(round(tmvalue(newseq),2)), str(round(tmvalue(newseq)-59.56, 2)))
        opt_val_list.append(round(tmvalue(newseq)-59.56, 2))
        newseq = newseq[:-1]
    optimal_val = min(opt_val_list)
    print('The optimal value is ' + str(opt_val_list.index(optimal_val)))
    return optimal_val

print(optimal_tm(r1))
print(optimal_tm(r2))