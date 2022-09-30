import sys

sys.stdin = open('B14719.txt')

H,W=map(int,input().split())
A=list(map(int,input().split()))
M=[]
m = -1
for i in range(len(A)-1,-1,-1):
	if m < A[i]: m = A[i]
	M = [m] + M

R = 0
m = A[0]
for i in range(1, len(A)-1):
	t = min(m, M[i]) - A[i]
	if t > 0: R += t
	if m < A[i]: m = A[i]
print(R)