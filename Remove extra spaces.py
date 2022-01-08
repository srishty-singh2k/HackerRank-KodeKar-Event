""" Given a string, remove any extra spaces from it.

Input Format:
Input a string.

Constraints:
string

Output Format:
Display that string after removing the extra spaces.

Sample Input:
hey   guys

Sample Output:
hey guys
"""

string = input()
strList = string.split(" ")

for str in strList:
    if len(str) != 0 :
        print(str, end=' ')
        
