from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return next(iter(diff))
    
    # return list(diff.keys())[0]
    # 리스트를 새로 만들어야 해서 메모리 낭비가 있음