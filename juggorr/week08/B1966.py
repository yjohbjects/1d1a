import sys
sys.stdin = open('B1966.txt')
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    score = list(map(int, input().split()))
    Q = deque([])

    for i in range(len(score)):
        if i == M:
            Q.append([score[i], 1])
        else:
            Q.append([score[i], 0])
                
    while Q:
        while True:
            
