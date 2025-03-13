# import heapq

# class DualPriorityQueue:
#     def __init__(self):
#         self.min_heap = []  # 최소 힙 (최솟값 저장)
#         self.max_heap = []  # 최대 힙 (최댓값 저장, 음수로 저장)
#         self.entry = {}  # 값이 현재 존재하는지 추적하는 딕셔너리

#     def insert(self, num):
#         """ 숫자 삽입 """
#         heapq.heappush(self.min_heap, num)
#         heapq.heappush(self.max_heap, -num)
#         self.entry[num] = self.entry.get(num, 0) + 1  # 값 카운팅

#     def delete_max(self):
#         """ 최댓값 삭제 """
#         self.sync_heaps()
#         if self.max_heap:
#             max_val = -heapq.heappop(self.max_heap)  # 최대 힙에서 최댓값 제거
#             if self.entry.get(max_val, 0) > 0:
#                 self.entry[max_val] -= 1  # 동기화

#     def delete_min(self):
#         """ 최솟값 삭제 """
#         self.sync_heaps()
#         if self.min_heap:
#             min_val = heapq.heappop(self.min_heap)  # 최소 힙에서 최솟값 제거
#             if self.entry.get(min_val, 0) > 0:
#                 self.entry[min_val] -= 1  # 동기화

#     def sync_heaps(self):
#         """ 동기화되지 않은 값 제거 """
#         while self.min_heap and self.entry.get(self.min_heap[0], 0) == 0:
#             heapq.heappop(self.min_heap)
#         while self.max_heap and self.entry.get(-self.max_heap[0], 0) == 0:
#             heapq.heappop(self.max_heap)

#     def get_result(self):
#         """ 최댓값과 최솟값 반환 """
#         self.sync_heaps()
#         if not self.min_heap or not self.max_heap:
#             return [0, 0]
#         return [-self.max_heap[0], self.min_heap[0]]

# def solution(operations):
#     dpq = DualPriorityQueue()  # 객체 생성

#     for operation in operations:
#         command, *value = operation.split()
#         if command == "I":
#             dpq.insert(int(value[0]))  # 삽입
#         elif command == "D" and dpq.entry:
#             if value[0] == "1":
#                 dpq.delete_max()  # 최댓값 삭제
#             elif value[0] == "-1":
#                 dpq.delete_min()  # 최솟값 삭제

#     return dpq.get_result()

# !최적화
# entry 딕셔너리 사용 -> 	exist set으로 존재 여부 관리
# sync_heaps()가 여러 번 호출됨	-> delete_max()와 delete_min()에서 즉시 동기화
# 삭제 연산 후 entry를 감소시킴	-> exist.discard(num)로 간단하게 제거
import heapq

class DualPriorityQueue:
    def __init__(self):
        self.min_heap = []  # 최솟값 관리용 최소 힙
        self.max_heap = []  # 최댓값 관리용 최대 힙 (음수로 저장)
        self.exist = set()  # 현재 존재하는 숫자 관리

    def insert(self, num):
        """ 숫자 삽입 """
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -num)
        self.exist.add(num)  # 존재하는 숫자로 추가

    def delete_max(self):
        """ 최댓값 삭제 """
        self.sync_heaps()
        if self.max_heap:
            max_val = -heapq.heappop(self.max_heap)
            self.exist.discard(max_val)  # 존재 목록에서 제거

    def delete_min(self):
        """ 최솟값 삭제 """
        self.sync_heaps()
        if self.min_heap:
            min_val = heapq.heappop(self.min_heap)
            self.exist.discard(min_val)  # 존재 목록에서 제거

    def sync_heaps(self):
        """ 힙에서 존재하지 않는 값 제거 (불필요한 pop 최소화) """
        while self.min_heap and self.min_heap[0] not in self.exist:
            heapq.heappop(self.min_heap)
        while self.max_heap and -self.max_heap[0] not in self.exist:
            heapq.heappop(self.max_heap)

    def get_result(self):
        """ 최댓값과 최솟값 반환 """
        self.sync_heaps()
        if not self.exist:
            return [0, 0]
        return [-self.max_heap[0], self.min_heap[0]]

def solution(operations):
    dpq = DualPriorityQueue()  # 객체 생성

    for operation in operations:
        command, *value = operation.split()
        if command == "I":
            dpq.insert(int(value[0]))  # 삽입
        elif command == "D":
            if value[0] == "1":
                dpq.delete_max()  # 최댓값 삭제
            elif value[0] == "-1":
                dpq.delete_min()  # 최솟값 삭제

    return dpq.get_result()
