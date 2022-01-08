"""If Give an integer N .
Write a program to obtain the sum of the first and last digits of this number.

Input Format:
Input an integer n.

Constraints:
1 ≤ n ≤ 1000000

Output Format:
Display the sum of the first and last digit of that number.

Sample Input:
1234

Sample Output:
5
"""

num = int(input())
sum = 0
first = num
last = num % 10
while (first >= 10):
    first /= 10
sum = int(first) + last
print(sum)
