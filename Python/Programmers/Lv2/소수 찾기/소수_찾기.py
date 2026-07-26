from itertools import permutations
import math

def is_prime(x):
    # 1은 소수에서 제외
    if x < 2:
        return False
        
    # 2는 소수
    if x == 2:
        return True
        
    # 2 외의 짝수는 소수에서 제외
    if x % 2 == 0:
        return False
        
    r = int(math.isqrt(x))
    for d in range(3, r + 1, 2):
        # 1과 자기자신이 아닌 다름 수로 나누어 떨어지면 소수 X
        if x % d == 0:
            return False
            
    return True

def solution(numbers):
    made = set()
    n = len(numbers)

    # 길이 1 ~ n 까지 모든 순열 생성
    for k in range(1, n + 1):
        for p in permutations(numbers, k):
            made.add(int(''.join(p)))  # 앞의 0은 int 변환 시 자연스럽게 처리됨

    return sum(1 for x in made if is_prime(x))