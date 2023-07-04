#疑似コード
'''##procedure Ex1 begin
A =[6,2,1,5,3,0,5,6,5]
    i= 1
    x = 1
    while A[i] != 0
        x = x * A[i]
        i= i + 1
    end while 
end
'''
#リストに0が出るまで掛け算を繰り返す
#最後にprint(x)でxの中身を表示
A = [6,2,1,5,3,0,5,6,5]
i = 0
x = 1
while A[i] != 0:
   x = x * A[i]
   i = i + 1
#各段階を可視化するために以下のprintを追加した
   print("Step " + str(i) + ": " + str(x))
print(x)
