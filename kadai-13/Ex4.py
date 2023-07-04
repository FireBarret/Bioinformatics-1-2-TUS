# TABで一段さげて、ここに関数subの内容を記述
def sub(y):
    if y == 0:
        return 1
    else:
        m = 0
#各段階を可視化するためにprint(m)を追加した
        m = sub(y-1)
        print(m)
        return m * y    
#メイン
print(sub(4))
