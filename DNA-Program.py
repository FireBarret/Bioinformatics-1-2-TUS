class DNA:
    def __init__(self, seq, name):
        self.seq = seq
        self.name = name
        self.salt_concentration = 0.5
        self.length = len(seq)
        self.GCper = round(DNA.GCratio(seq), 2)
        self.Tm = round(DNA.tmvalue(seq), 2)
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
        Tm = round(81.5 + (16.6 * (-1.3)) + (0.41 * DNA.GCratio(seq)) - (500/len(seq)), 2)
        return Tm
    def info_DNA(self):
        print('Sequence: ' + self.seq)
        print('Name: ' + self.name)
        print('Salt concentration: ' + str(self.salt_concentration))
        print('Length: ' + str(self.length))
        print('GC percentage: ' + str(self.GCper))
        print('Tm value: ' + str(self.Tm))
f1 = DNA('ATGGCTATGATGGAGGTCCAGG', 'f1')
r1 = DNA('TTAGCCAACTAAAAAGGCCCCAAAAAAACTGG', 'r1')
r2 = DNA('TTATTTTGCGGCCCAGAGCCTTTTCATTCTTG', 'r2')
f1.info_DNA()
r1.info_DNA()
r2.info_DNA()