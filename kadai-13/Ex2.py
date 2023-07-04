'''
#疑似コード
procedure Ex2 begin
    A=[5,3,6,4]
    B=[1,3,4]
    x=0
    for i=1 to 4
        for j=1 to 3
            x = x + A[i] * B[j]
        end for
    end for
end 
'''

#最後にprint(x)でxの中身を表示
A = [5,3,6,4]
B = [1,3,4]
x = 0
y = 0 
z = 0
for i in range(len(A)):
    for j in range(len(B)):
        z = y
        y = x
        x = x + A[i] * B[j]
#各段階を可視化するために以下のprintを追加した
    print("Step " + str(i+1) + ": " + str(z) + "->" + str(y) + "->" + str(x))
print("最後の戻り値は:" + str(x))
