# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.
def createDictionary():
    dict = {'Привет' : 'Привет!', 'Как тебя зовут?' : 'Меня зовут Анатолий'}
    while True:
        text = input('Введите фразу: ')
        findAnswer = 0
        for k in dict.keys():
            if text == k:
                print(dict[k])
                findAnswer = 1
                break
        if findAnswer == 0:
            if text == 'Пока':
                break    
            else:
                text2 = input('Как бы вы ответили на этот вопрос? Напишите: ')
                dict.update({text : text2})
    return dict
createDictionary()
    
