import sys
input = sys.stdin.readline


n = int(input())
lst = [0,1,1]

for i in range(3,21):
    lst.append( lst[i-1] + lst[i-2])

print(lst[n])