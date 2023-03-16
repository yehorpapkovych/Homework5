import random

my_list1 = []
my_list2 = []
i = 0
while i < 10:
    my_list1.append(random.randint(1, 10))
    my_list2.append(random.randint(1, 10))
    i += 1
n = 1
my_list3 = []
while n <= 10:
    if my_list1.count(n) > 0 and my_list2.count(n) > 0:
        my_list3.append(n)
    n += 1
print(my_list1, my_list2)
print(my_list3)