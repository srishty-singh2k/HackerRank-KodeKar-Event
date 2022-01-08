"""Given a string S, the task is to create a string with the first letter of every word in the string.

Input Format:
Input a string.

Constraints:
1 <= |S| <= 105

Output Format:
print a string containing the first letter of every word from the previous string.

Sample Input:
hello guys

Sample Output:
hg
"""

str = input()
strList = str.split()
for s in strList:
    print( s[0], end='')
