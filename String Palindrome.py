"""
Check whether a given string is palindrome or not.
If yes print "1" and if no print "0"

Note:- A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.

Input Format:
Input a string.

Constraints:
Only Characters.

Output Format:
Print "1" for yes and "0" for no

Sample Input:
abba

Sample Output:
1

Explanation:
Reverse of abba is abba which shows it is a palindrome string that's why its output is 1.

"""


word = input()
revWord = word[::-1]
if word == revWord :
    print ("1")
else :
    print ("0")
