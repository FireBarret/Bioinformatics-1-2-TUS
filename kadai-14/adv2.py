import datetime
year = datetime.datetime.today().year
age = year - int(input("生まれた年を入力してください: "))
height = int(input("伸長を入力してください:(cm) "))
weight = int(input("体重を入力してください：(kg)"))
## BMI ＝ 体重kg ÷ (身長m)^2
def bmi_val(height, weight):
    return weight / ((height/100)**2)
def health_check(age, height, weight):
    bmi = bmi_val(height, weight)
    if age < 18:
        print("🐤18歳未満のため、判定できません")
    elif bmi < 18.5:
        print("🍗低体重、もう少し食べましょう〜")
    elif 18.5 <= bmi < 25:
        print("😃普通体重、健康的ですね〜")
    elif 25 <= bmi < 30:
        print("🤤肥満（１度）、ぽっちゃりは幸福の証とも言われます〜")
    elif 30 <= bmi < 35:
        print("🙁肥満（２度）、健康に気をつけましょう〜")
    elif 35 <= bmi < 40:
        print("☹️肥満（３度）、頑張って痩せましょう！")
    else:
        print("💀肥満（４度）、死に至る恐れがあるので、痩せましょう！")
health_check(age, height, weight)






