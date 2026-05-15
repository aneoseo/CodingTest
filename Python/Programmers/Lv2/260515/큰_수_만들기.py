# O(k*n)

# def solution(number, k):

#     # 바로 뒷 숫자보다 작으면 제거 -> k번 반복
#     # 바로 뒷 숫자보다 작은 수가 없는 경우 -> 맨 뒷 숫자 제거
    
#     for i in range(k):
#         rm = False
        
#         for j in range(len(number)-1):
#             if number[j] < number[j+1]:
#                 number = number[:j] + number[j+1:]
#                 rm = True
#                 break
#             else:
#                 continue
        
#         if rm == False:
#             number = number[:-1]
    
#     return number


# 스택
# O(n)

def solution(number, k):
    stack = []
    rm_cnt = k

    for num in number:
		# 스택의 맨 끝이 현재 숫자보다 작으면 제거
        while stack and rm_cnt > 0 and stack[-1] < num:
            stack.pop()
            rm_cnt -= 1

        stack.append(num)

    if rm_cnt > 0:
        stack = stack[:-rm_cnt]

    return ''.join(stack)