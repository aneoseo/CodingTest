from collections import deque

def solution(priorities, location):
    queue = deque()
    order = 0

    for i, p in enumerate(priorities):
        queue.append((i, p))

    while queue:
        i, p = queue.popleft()

        if any(p < q[1] for q in queue):
            queue.append((i,p))
        else:
            order += 1
            if location == i:
                return order