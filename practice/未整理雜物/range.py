arr1 = []
for i in range(10):
    arr1.append(i)
print(arr1)
print('*******')
arr1 = [i for i in range(10)]
arr2 = [x for x in arr1 if x % 2 == 0]
arr3 = [x for x in arr1 if x > 3 and x % 2]
arr4 = [(x,y) for x in range(3) for y in range(4)]
print(arr1)
print(arr2)
print(arr3)
print(arr4)

print('********')

