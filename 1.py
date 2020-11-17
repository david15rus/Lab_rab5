from random import random
N = 10
arr = []
for i in range(N):
    arr.append(int(random() * 30) - 5)
print(arr)

neg = -1
for i in range(N):
    if arr[i] < 0:
        neg = i
        break

if neg == -1:
    print('Отрицательных нет')
else:
    print('Номер первого отриц.:', neg+1)
    s = 0
    for i in range(neg+1,N):
        s += abs(arr[i])
    print('Сумма: ', s)