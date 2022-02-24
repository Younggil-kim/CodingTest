# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
#
# grp = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for i in range(m):
#     a,b,c = map(int, input().split())
#     grp[a].append((b,c))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in grp[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))
#
# start, end = map(int, input().split())
# dijkstra(start)
# print(distance)






import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

grp = [[] for _ in range(n+1)]
distance = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    grp[a].append((b,c))


def dijkstra(start):
    que = []
    heapq.heappush(que, (0,start))
    distance[start] = 0
    while que:

        dist, now = heapq.heappop(que)
        # 현재 설정된 거리보다 길다면 패스
        if distance[now] < dist:
            continue
        #그게 아니라면
        #거기서부터 갈수있는 곳 모두 돌아서 갱신
        for i in grp[now]:
            cost = dist + i[1]
            # 만약 거기서부터 갈 수 있는 곳까지의 비용이
            # 지금 설정된 거리보다 작으면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])