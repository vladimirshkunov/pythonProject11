age1 = int(input('Возраст А: '))
age2 = int(input('Возраст Б: '))
age3 = int(input('Возраст В: '))
if age1 == age2 == age3:
    print('Все одного возраста')
elif age1 == age2 > age3:
    print('А и Б старше В')
elif age3 == age2 > age1:
    print('B и Б старше A')
elif age1 == age3 > age1:
    print('А и В старше Б')
elif age1 > age2 and age1 > age3:
    print('А старше всех')
elif age2 > age3 and age2 > age1:
    print('Б старше всех')
elif age3 > age2 and age3 > age1:
    print('В старше всех')

