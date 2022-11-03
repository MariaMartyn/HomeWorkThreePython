#Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
def DictionaryFruit():
    data = open('task2.txt', encoding='utf-8')
    fruit = data.readlines()
    data.close
    new_fruit = []
    letter = input('Введите букву для поиска фрукта: ')
    for i in fruit:
        if i[0] == letter.upper():
            new_fruit.append(i)
    return(new_fruit)
print(DictionaryFruit())