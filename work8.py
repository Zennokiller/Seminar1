# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("n= "))
m = int(input("m= "))
k = int(input("k= "))
if (k % n == 0) and (n*m>k):
    print("yes")
elif (k % m == 0) and (n*m>k):
    print("yes")
else:
    print("no")
