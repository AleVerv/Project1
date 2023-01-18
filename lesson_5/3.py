#не совсем разобралась с этим

while True:
age = int(input())
name = input()
if age <= 0 or type(age) == str:
    print("Ошибка, повторите ввод")
elif age > 0 and age < 10:
    print(f"Привет, шкет {name}")
elif 10 > age > 18:
    print(f"Как жизнь {name}?")
elif 18 > age > 100:
    print(f'Что желаете {name}?')
else:
    print(f'{name}, вы лжете - в наше время столько не живут...')