my_list1 = list(range(1, 101))
my_list2 = []
i = 0
while i < 100:
    if my_list1[i] % 7 == 0 and my_list1[i] % 5 != 0:
        my_list2.append(my_list1[i])
    i += 1
print(my_list2)