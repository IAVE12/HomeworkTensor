list = [1, 3, 2, 5 ,9, 11, 10 , 21]
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)