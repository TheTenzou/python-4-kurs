number_count = [0]*10
for _ in range(int(input("num count:"))):
    number = input("number:")
    number_count[len(number)-1] += 1
min_number_count = 10_001
mini = 0
for i in range(len(number_count)):
    if number_count[i] < min_number_count and number_count[i] > 0:
        min_number_count = number_count[i]
        mini = i
print(mini+1, min_number_count)