import random

sum = 0 

for i in range(10):
    x = random.randint(1, 6)
    sum += x  
    print(str(i + 1) + "回目：" + str(x))

average = total / 10 
print("平均：" + str(round(average, 1)))  


# 期待される出力結果例
"""

1回目：3
2回目：6
3回目：2
4回目：5
5回目：4
6回目：1
7回目：6
8回目：3
9回目：2
10回目：4
平均：3.6
"""
