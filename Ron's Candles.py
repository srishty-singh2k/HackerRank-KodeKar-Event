count = 0
n = int(input())
for num in range(2, n+1):
       for i in range(2, num):
           if ((num % i) == 0):
               count = count + 1
               print("Next: ", num)
print("ans: ", count-1)
