house, money = map(int, input().split())

if house%2 == 0 :
    print(int((house/2)*money))
else:
    print(int(((house+1)/2)*money))
