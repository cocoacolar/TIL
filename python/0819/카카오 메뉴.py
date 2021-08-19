from itertools import combinations
def solution(orders, course):
    nworders = []
    for i in orders:
        x = [ord(a) for a in i]
        nworders.append(x)
    for order in nworders:
        order.sort()
        for w in range(len(order)):
            order[w] = chr(order[w])

    result = []
    for c in course:
        tmp = []
        for m in nworders:
            mc = list(combinations(m, c))
            tmp += mc

        tem = []
        big = 0
        for a in tmp:
            if tmp.count(a) >= 2:
                if big < tmp.count(a):
                    big = tmp.count(a)
                    tem =[]
                    tem.append(a)
                elif big == tmp.count(a) and a not in tem:
                    tem.append(a)

        for r in tem:
            word = ''
            for o in r:
                word += o
            result.append(word)
    result.sort()
    return result