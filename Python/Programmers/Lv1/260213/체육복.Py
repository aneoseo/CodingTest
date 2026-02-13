# for문 사용

# def solution(n, lost, reserve):
#     # 정렬 (이 문제에서 필수는 아니지만, 일반적으로 그리디 처리 시 안정적)
#     lost.sort()
#     reserve.sort()
    
#     # 자신이 여벌을 갖고 있었는데 도난도 당한 경우
#     for l in lost[:]:    # lost가 아니라 lost의 복사본(lost[:])을 순회
#         if l in reserve:
#             lost.remove(l)
#             reserve.remove(l)

#     # 그리디하게 앞번호, 뒷번호 확인하며 빌려주기
#     for r in reserve[:]:    # reserve가 아니라 reserve의 복사본(reserve[:])을 순회
#         if r - 1 in lost:
#             lost.remove(r - 1)
#         elif r + 1 in lost:
#             lost.remove(r + 1)
            
#     return n - len(lost)


# set 사용 (성능 개선)

def solution(n, lost, reserve):
    # 자신이 여벌을 갖고 있었는데 도난도 당한 경우
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    lost = lost_set - reserve_set
    reserve = reserve_set - lost_set

    # 그리디하게 앞번호, 뒷번호 확인하며 빌려주기
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
            
    return n - len(lost)
