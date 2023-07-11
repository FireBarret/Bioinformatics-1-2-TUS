def multiple_of_3(x):
    if x % 3 == 0 and x % 10 == 3:
        print("3の倍数であり、数字の最後に3がつきます")
    elif x % 3 == 0:
        print("3の倍数ですよ")
    elif x % 10 == 3:
        print("数字の最後に3がつきます")
    else:
        print("3の倍数ではありません")
        
#test code
for i in range(1, 41):
    print(i, end=" ")
    multiple_of_3(i)
