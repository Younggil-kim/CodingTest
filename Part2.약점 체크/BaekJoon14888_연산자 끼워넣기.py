import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))
lst = []
def recursive(result,idx,add,sub,mul,div):
    if add == 0 and sub == 0 and mul == 0 and div == 0:
        lst.append(result)
    else:
        if add > 0:
            recursive(result + nums[idx], idx+1, add-1, sub, mul, div )
        if sub > 0:
            recursive(result - nums[idx], idx+1, add, sub-1, mul, div)
        if mul > 0:
            recursive(result * nums[idx], idx +1, add, sub, mul-1, div)
        if div > 0:
            recursive(int(result / nums[idx]), idx +1, add, sub, mul, div-1)

recursive(nums[0],1, cal[0],cal[1],cal[2],cal[3])

print(max(lst))
print(min(lst))