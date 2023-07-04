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


#最後にprint(x)でxの中身を表示
print(x)

