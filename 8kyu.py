numbers = [2, 5, 6, 7]
numbers2 = []

for i in range(len(numbers)):
    if i == 0 and numbers[i] == 0 or i != 0 and numbers[i] % i == 0:
        numbers2.append(numbers[i])
            


for a in numbers2:
            print(a)