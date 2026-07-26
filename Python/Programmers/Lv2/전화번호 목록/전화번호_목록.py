# 정렬: O(n log n) / 구현 빠름

# def solution(phone_book):
#     phone_book.sort()
    
#     for i in range(len(phone_book) - 1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
    
#     return True


# 해시: O(n) / 코드 김

def solution(phone_book):
    # 해시 저장
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 1
    
    # 각 번호가 접두어로 포함되는게 있는지 확인
    for phone in phone_book:
        prefix = ""
        for char in phone:
            prefix += char
            if prefix in hash_map and prefix != phone:  # 자기 자신은 제외
                return False
    
    return True