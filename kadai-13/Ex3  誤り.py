def sub():
# TABで一段さげて、ここに関数subの内容を記述
    x = float(input("xの値を入力してください:"))
    y = float(input("yの値を入力してください"))
#ここでは、xとyの引き算は整数であるかどうかを判定する
#整数であれば、整数として返す
#整数でなければ、小数2まで返す    
    if (x - y).is_integer():
        return int(x - y)
    else: return round(x - y, 2)
    
#関数subに引数10を与えてprint
print(sub())
