# coding: Shift-JIS
import math

seq = "AGCTCGTACGTCATCATACCA"
x = 0
for i in range(0, len(seq)):
    if seq[i] == "G" or seq[i] == "C":
        x = x + 1
    else:
        x = x + 0
GCper = round(x/len(seq)*100, 2)
print("GC割合は"+ str(GCper)+ "%である。")  

# PCR反応について、あるプライマーに対してTm値を計算する。
# Tm値は、プライマーの塩基配列の長さによって変化する
# Tm値の計算式は Tm= 81.5+(16.6*(log10(塩濃度)))+(0.41*GC割合)-(500/プライマリーの長さ)

# input は　str であるため、floatに変換する必要がある。
# log10はmath.log10()で計算できる。
salt = math.log10(float(input('Please insert salt concentration(M))')))

Tm = round(81.5 + (16.6 * salt) + (0.41 * GCper) - (500/len(seq)), 2)
print("Tm値は"+str(Tm)+"°Cである。")
print("Annealing 温度は"+str(round(Tm-3))+"°Cである。")