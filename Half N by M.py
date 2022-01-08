num, div = map(int, input().split())

while div>1 :
    num = num / 2
    div -= 1
print(int(num))
