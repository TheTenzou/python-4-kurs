numbers = list()
for t in range(int(input())):
    number = input()
    digit_count = len(number)
    flag = True
    for i in range(len(numbers)):
        if numbers[i][0] == digit_count:
            numbers[i][1] += 1
            flag = False
    if flag:
        numbers.append(list((digit_count, 1)))
numbers.sort(key=lambda item: item[0]+10_000*item[1])
print(numbers[0][0], numbers[0][1])
