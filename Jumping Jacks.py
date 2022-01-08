"""Once there was a boy named jack.
He was quite intelligent and was also fond of jumping.
But he jumped in a pattern like 1 leap, 2 leap, 3 leap and again from the start after 3rd leap.
1 leap means if Jack is at point P then he will jump to P+1.
2 leap means if Jack is at point P then he will jump to P+2.
3 leap means if Jack is at point P then he will jump to P+3.
Find whether he could land up to a point N or not.
Note- He starts from point 0.

Input Format:
Input an integer.

Constraints:
1<=N<=10^2

Output Format:
Print "yes" or "no".

Sample Input:
1
Sample Output"
yes

"""

num = int(input())
i = 0
while(i<500):
    for n in [1,2,3]:
        i+=n
        if num==i:
            print("yes")
            exit()
print("no")
    
