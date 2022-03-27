def solution(purchase):
    dates = [0 for _ in range(365)]

    def cvt(month, day):
        count = 0
        if month == 1:
            count += 0
        elif month == 2:
            count += 31  # 31 + day
        elif month == 3:
            count += 59
        elif month == 4:
            count += 90
        elif month == 5:
            count += 120
        elif month == 6:
            count += 151
        elif month == 7:
            count += 181
        elif month == 8:
            count += 212
        elif month == 9:
            count += 243
        elif month == 10:
            count += 273
        elif month == 11:
            count += 304
        elif month == 12:
            count += 334
        count += day
        return count - 1

    lst = []
    for i in purchase:
        i = i.split(' ')
        month = int(i[0][5] + i[0][6])
        day = int(i[0][8] + i[0][9])
        mon = int(i[1])
        lst.append([month, day, mon])
        start = cvt(month, day)
        for j in range(30):
            if start + j >= 365:
                break
            dates[start + j] += mon

    result = [0, 0, 0, 0, 0]
    for money in dates:
        if money < 10000:
            result[0] += 1
        elif 10000 <= money and money < 20000:
            result[1] += 1
        elif 20000 <= money and money < 50000:
            result[2] += 1
        elif 50000 <= money and money < 100000:
            result[3] += 1
        elif 100000 <= money:
            result[4] += 1
    return result