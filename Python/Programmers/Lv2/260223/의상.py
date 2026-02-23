def solution(clothes):
    closet = {}
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1
        
    # (A 종류 의상 개수 + 1(A 종류를 입지 않는 경우)) * (B + 1) * ...
    #  - 1(아무 옷도 선택하지 않은 경우)
    ans = 1
    for k in closet.values():
        ans *= (k + 1)

    return ans - 1