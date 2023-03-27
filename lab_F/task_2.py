#https://pythonist.ru/primery-resheniya-prostyh-zadach-na-yazyke-python/
#https://proglib.io/p/5-zadach-s-resheniyami-na-python-dlya-nachinayushchih-razrabotchikov-2022-04-25
#Напишите программу, решающую задачу на python
#https://ru.stackoverflow.com/questions/1033594/%D0%9F%D0%BE%D0%BC%D0%BE%D0%B3%D0%B8%D1%82%D0%B5-%D1%80%D0%B5%D1%88%D0%B8%D1%82%D1%8C-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D1%83-%D0%BD%D0%B0-python
#Напишите программу, решающую задачу
#https://www.cyberforum.ru/python-beginners/thread2693998.html
#вывод сумм одинаковых чисел пайтон
#https://www.cyberforum.ru/python-beginners/thread2693998.html
#
#

n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
    print(i, sep=" ",end=" ")
    if(i < n):
        print("+", sep=" ", end=" ")
    a.append(i)
print("=", sum(a))