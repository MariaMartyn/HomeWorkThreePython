#Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def FindFibonacci():
    N = int(input('Введите число N: '))
    fibonacci = [0, 1]
    for i in range(1, N):
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
    return(fibonacci)
    

result = str(FindFibonacci())
print(result)

data = open('task1.txt', 'w')
data.writelines(result)
data.close

