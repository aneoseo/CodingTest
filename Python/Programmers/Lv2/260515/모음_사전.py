def solution(word):
    vowels = "AEIOU"
    # 각 자리에서 글자가 하나 뒤로 밀릴 때 건너뛰는 단어 수
    weights = [1 + 5 + 5**2 + 5**3 + 5**4, 
               1 + 5 + 5**2 + 5**3, 
               1 + 5 + 5**2, 
               1 + 5, 
               1]
    
    # 현재 글자 수 + 현재 글자보다 앞선 순서의 글자들로 인해 건너뛰는 단어 수
    answer = len(word)
    for i, ch in enumerate(word):
        answer += vowels.index(ch) * weights[i]

    return answer