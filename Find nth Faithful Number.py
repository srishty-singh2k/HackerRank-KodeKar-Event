"""A number is called faithful if you can write it as the sum of distinct powers of 7.
e.g. 2457 = 7 + 7^2 + 7^4.
If we order all the faithful numbers, we get the sequence 1 = 7^0, 7 = 7^1, 8 = 7^0 + 7^1, 49 = 7^2, 50 = 7^0 + 7^2 . . . and so on.
Given some value of N, you have to find the N'th faithful number

Input Format:
Input an integer.

Constraints:
1<=N<=10^3

Output Format:
Print the nth faithful number.

Sample Input:
3
Sample Output:
8
Explanation:
8 is the 3rd faithful number 8 = 7^0 + 7^1 """


num = int(input())
i=0
sum=0
bnum = bin(int(num)).replace("0b", "")
for digit in str(bnum):
    sum+=(int(digit)*(pow(7,i)))
    i+=1
print(sum)
