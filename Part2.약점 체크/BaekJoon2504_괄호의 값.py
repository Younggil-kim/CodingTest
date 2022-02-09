
strs = input()
left =[]
flag = False

for pa in strs:
    if pa == "(" or pa == "[":
        left.append(pa)
    else:
        if pa == ")":
            if not left:
                flag = True
                break
            cur = 0
            while True:
                if not left:
                    flag = True
                    break
                tmp = left.pop()
                if tmp == "(":
                    if cur == 0:
                        left.append(2)
                        break
                    else:
                        left.append(cur*2)
                        break
                elif tmp == "[":
                    flag = True
                    break
                else:
                    cur = cur + tmp
        elif pa == "]":
            if not left:
                flag = True
                break
            cur = 0
            while True:
                if not left:
                    flag = True
                    break
                tmp = left.pop()
                if tmp == "[":
                    if cur == 0:
                        left.append(3)
                        break
                    else:
                        left.append(cur*3)
                        break
                elif tmp == "(":
                    flag = True
                    break
                else:
                    cur = cur + tmp
        if flag:
            break

if "(" in left or "[" in left or ")" in left or "]" in left or flag:
    print(0)
else:
    print(sum(left))


