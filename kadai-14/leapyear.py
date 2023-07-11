import datetime
year = datetime.datetime.today().year
## 応用問題2

age = year - int(input("生まれた年を入力してください: "))
x = int(input("伸長を入力してください:(cm) "))
y = int(input("体重を入力してください："))
print(age)
def BMI(age, x, y):
    return y / (x)**2
def health_check(age, x, y):
    if age < 18:
        print("🐤18歳未満のため、判定できません")
    elif BMI(age, x, y) < 18.5:
        print("🍗低体重、もう少し食べましょう〜")
    elif 18.5 <= BMI(age, x, y) < 25:
        print("😃普通体重、健康的ですね〜")
    elif 25 <= BMI(age, x, y) < 30:
        print("🤤肥満（１度）、ぽっちゃりは幸福の証とも言われます〜")
    elif 30 <= BMI(age, x, y) < 35:
        print("🙁肥満（２度）、健康に気をつけましょう〜")
    elif 35 <= BMI(age, x, y) < 40:
        print("☹️肥満（３度）、頑張って痩せましょう！")
    else:
        print("💀肥満（４度）、死に至る恐れがあるので、痩せましょう！")
## BMI ＝ 体重kg ÷ (身長m)2
health_check(age, x, y)





