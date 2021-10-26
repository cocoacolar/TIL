import sys
input = sys.stdin.readline
# sys.stdin = open('백만개.txt')


def partition(A, l, r):
	p = A[l]
	i, j = l, r
	while i<=j:
		while i<=j and A[i]<=p:
			i += 1
		while i<=j and A[j]>=p:
			j -= 1
		if i<j:
			A[i], A[j] = A[j], A[i]
	A[l], A[j] = A[j], A[l]
	return j

def quick_sort(A, l, r):
	if l<r:
		s = partition(A, l, r)
		quick_sort(A, l, s-1)
		quick_sort(A, s+1, r)

N = int(input())
arr = [0] * 10001
for i in range(N):
	k = int(input())
	arr[k] += 1
# quick_sort(arr, 0, len(arr)-1)
for k in range(1, 10001):
	for i in range(arr[k]):
		print(k)