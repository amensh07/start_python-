my_task_5 = open("task_hw_5.txt", 'w', encoding="utf-8")
my_num = [el for el in range(10, 100) if el % 8 == 0]
print(my_num)


def listsum(my_num):
    list_sum = 0
    for i in my_num:
        list_sum = list_sum + i
    return list_sum

print(listsum(my_num))
my_task_5.close()
