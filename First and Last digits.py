num = int(input())
sum = 0
first = num
last = num % 10
while (first >= 10):
    first /= 10
sum = int(first) + last
print(sum)
