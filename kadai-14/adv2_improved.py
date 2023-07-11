
import datetime
def get_user_input(prompt, error_message, conversion_function=int):
    while True:
        try:
            return conversion_function(input(prompt))
        except ValueError:
            print(error_message)
def get_current_year():
    return datetime.datetime.today().year

def calculate_age(birth_year):
    return get_current_year() - birth_year

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def print_health_assessment(age, bmi):
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

def main():
    birth_year = get_user_input("生まれた年を入力してください (例: 2000): ", "無効な年です。再度入力してください。")
    height = get_user_input("身長を入力してください (cm) (例: 170): ", "無効な身長です。再度入力してください。")
    weight = get_user_input("体重を入力してください (kg) (例: 70): ", "無効な体重です。再度入力してください。")

    age = calculate_age(birth_year)
    bmi = calculate_bmi(height, weight)

    print_health_assessment(age, bmi)

# Run the main function
# main()
