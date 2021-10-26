# T = int(input())
#
# for tc in range(1, T+1):
#     s_1 = input()
#     s_2 = input()
#     k = len(s_1)
#     for i in range(len(s_2)-k+1):
#         if s_2[i:i+k] == s_1:
#             print(f'#{tc} 1')
#             break
#     else:
#         print(f'#{tc} 0')

a = ['absddcsd', 'asdgr']
print(a[0][2:5][::-1])