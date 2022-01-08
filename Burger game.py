""" Write a program that takes a number and returns its multiplicative persistence, which is the number of times you must multiply the digits in number until you reach a single digit.
Examples bugger(39) ➞ 3 // Because 3 * 9 = 27, 2 * 7 = 14, 1 * 4 = 4 and 4 has only one digit.
bugger(999) ➞ 4 // Because 9 * 9 * 9 = 729, 7 * 2 * 9 = 126, 1 * 2 * 6 = 12, and finally 1 * 2 = 2.

Input Format:
Input consists single integer N.

Constraints:
1<=N<=10^6

Output Format:
Output consists an integer.

Sample Input:
39

Sample Output:
3
"""

def count(n):
    count = 0
    while(n>0):
        r = n%10
        count+=1
        n = n//10
    return count

def add(n):
    s = 1
    while(n>0):
        r = n%10
        s = s*r
        n = n//10
    return s

n = int(input())
c = 0
s = 0
while(count(n)!=1):
    n = add(n)
    c+=1
print(c)
