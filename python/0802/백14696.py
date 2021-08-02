'''
두 어린이 A, B가 딱지놀이를 한다. 딱지놀이 규칙은 다음과 같다. 두 어린이는 처음에 여러 장의 딱지를 가지고 있고, 매 라운드마다 각자 자신이 가진 딱지 중 하나를 낸다. 딱지에는 별(★), 동그라미(●), 네모(■), 세모(▲), 네 가지 모양 중 하나 이상의 모양이 표시되어 있다. 두 어린이가 낸 딱지 중 어느 쪽이 더 강력한 것인지는 다음 규칙을 따른다.

만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
예를 들어, 두 어린이 A, B가 낸 딱지가 다음 그림과 같다고 하자.

별 = 4, 동그라미 3 , 네모 2, 세모 1

'''

import sys

def count_model(A, B, model):
    if A[1:].count(model) > B[1:].count(model):
        return 'A'
    elif A[1:].count(model) < B[1:].count(model):
        return 'B'
    elif A[1:].count(model) == B[1:].count(model) and model !=  1:
        return count_model(A, B, model-1)
    elif  A[1:].count(model) == B[1:].count(model) and model ==  1:
            return 'D'


T = int(input())

for round in range(T):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    
    print(count_model(A, B, 4))


