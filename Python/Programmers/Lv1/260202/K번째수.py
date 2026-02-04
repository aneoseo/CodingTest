# 오답 코드

# def solution(array, commands):
#     answer = []
    
#     for i in range(len(commands)):
#         slicing_arr = array[commands[i][0]-1:commands[i][1]]
#         sorted_arr = slicing_arr.sort()
#         answer[i] = sorted_arr[commands[i][2]-1]
    
#     return answer


# 정답 코드

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        slicing_arr = array[commands[i][0]-1:commands[i][1]]
        sorted_arr = sorted(slicing_arr)
        answer.append(sorted_arr[commands[i][2]-1])
    
    return answer