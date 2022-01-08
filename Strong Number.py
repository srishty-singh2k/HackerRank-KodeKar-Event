"""Given a number N, print all the Strong Numbers less than or equal to N.

Note:- Strong number is a special number whose sum of the factorial of digits is equal to the original number.
For Example: 145 is strong number. Since, 1! + 4! + 5! = 145.

Input Format:
Input an integer.

Constraints:
1<=n<=1000

Output Format:
Print all the numbers which are strong.

Sample Input:
100

Sample Output:
1 2
"""

import math
num=int(input())  
  
for x in range(1, num+1) :
    temp = x
    sum = 0
    while(temp > 0):
        r = temp % 10
        fact = math.factorial(r)
        sum = sum + fact
        temp = temp // 10
    
    if(sum==x):  
        print(x, end=' ')    
