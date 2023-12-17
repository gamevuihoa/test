numbers = input().split()
N = int(numbers[0])
a = [int(x) for x in numbers[1:]]

total = 0
for num in a:
    total += num

print(total)
