num = int(input())
for i in range(1,num+1):
    for j in range(1,num-i+2):
        print ("*", end='')
    print()
