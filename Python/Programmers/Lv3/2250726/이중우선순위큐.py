import heapq

# 중복 코드 함수 분리 ver.
# def clean(heap, valid):
#    while heap and not valid[heap[0][1]]:
#        heapq.heappop(heap)

def solution(operations):
    min_heap = []
    max_heap = []
    valid = [False] * len(operations)   # 유효한 원소인지 확인
    
    for i, operation in enumerate(operations):
        op, value = operation.split()
        value = int(value)
        
        # 큐 삽입
        if op == "I":
            heapq.heappush(min_heap, (value, i))
            heapq.heappush(max_heap, (-value, i))
            valid[i] = True

        # 최댓값 삭제
        elif op == "D" and value == 1:
            # 무효(min_heap에서 이미 삭제된) 원소 제거
            while max_heap and not valid[max_heap[0][1]]:
                heapq.heappop(max_heap)
            # clean(max_heap, valid)

            if max_heap:
                _, idx = heapq.heappop(max_heap)
                valid[idx] = False

        # 최솟값 삭제
        elif op == "D" and value == -1:
            # 무효(max_heap에서 이미 삭제된) 원소 제거
            while min_heap and not valid[min_heap[0][1]]:
                heapq.heappop(min_heap)
            # clean(min_heap, valid)

            if min_heap:
                _, idx = heapq.heappop(min_heap)
                valid[idx] = False
    
    # 최종 결과를 구하기 전에 무효 원소 제거
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
    # clean(min_heap, valid)
    # clean(max_heap, valid)

    if not min_heap:
        return [0, 0]
    return [-max_heap[0][0], min_heap[0][0]]