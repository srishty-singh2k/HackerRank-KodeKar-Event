"""Find all the perfect squares between 1 to n.
NOTE:- Perfect squares are those numbers whose square root is a natural number. Example:- 1,4,9,16.

Input Format:
Input an integer n.

Constraints:
1<=n<=10^4

Output Format:
Print all the perfect squares between 1 to n.

Sample Input:
10

Sample Output:
1 4 9

"""

import math

num = int(input())

for n in range(1, num+1):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        print(n, end=' ')
