def find_insert_position(mas, x):
    if len(mas) == 0:
        return 0

    left, right = 0, len(mas) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mas[mid] == x:
            return mid
        elif mas[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return left


mas1 = [1, 2, 3, 3, 3, 5]
mas2 = [2, 3, 4]
mas3 = [1, 2, 3]
mas4 = []
x1 = 4
x2 = 1
x3 = 4
x4 = 6

res1=find_insert_position(mas1, x1)
res2=find_insert_position(mas2, x2)
res3=find_insert_position(mas3, x3)
res4=find_insert_position(mas4, x4)

print(find_insert_position(mas1, x1))
print(find_insert_position(mas2, x2))
print(find_insert_position(mas3, x3))
print(find_insert_position(mas4, x4))

mas1.insert(res1, x1)
mas2.insert(res2, x2)
mas3.insert(res3, x3)
mas4.insert(res4, x4)

print(mas1 == sorted(mas1))
print(mas2 == sorted(mas2))
print(mas3 == sorted(mas3))
print(mas4 == sorted(mas4))
