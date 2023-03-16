import random

my_list = []
i = 0
while i < 10:
    my_list.append(random.randint(1, 100))
    i += 1
m = my_list[0]
for _ in my_list:
    if _ > m:
        m = _
print(my_list, m)