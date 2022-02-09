
import sys
input = sys.stdin.readline

def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

a,b = map(int, input().split())

print(GCD(a,b))
print(LCM(a,b))