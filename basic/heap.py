# implement heap
import heapq
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx-1)//2

    def leftChild(self, idx):
        return 2*idx + 1

    def rightChild(self, idx):
        return 2*idx + 2

    def insert(self, num):
        self.heap.append(num)
        self.siftUp(len(self.heap)-1)

    def siftUp(self, idx):
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]
            idx = self.parent(idx)

    def extract(self):
        if not self.heap: return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapify()
        return root

    def heapify(self,idx=0):
        sm = idx
        left = self.leftChild(idx)
        right = self.rightChild(idx)

        if left < len(self.heap) and self.heap[left] < self.heap[sm]:
            sm = left
        if right < len(self.heap) and self.heap[right] < self.heap[sm]:
            sm = right

        if sm != idx:
            self.heap[sm], self.heap[idx] = self.heap[idx], self.heap[sm]
            self.heapify(sm)

    def peek(self):
        if self.heap[0]: return self.heap[0]

    def buildHeap(self, arr):
        self.heap = arr
        for i in range((len(arr)//2)-1,-1,-1):
            self.heapify(i)

    def size(self):
        return len(self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx-1)//2

    def leftChild(self, idx):
        return 2*idx + 1

    def rightChild(self, idx):
        return 2*idx + 2

    def insert(self, num):
        self.heap.append(num)
        self.siftUp(len(self.heap)-1)

    def siftUp(self, idx):
        while idx > 0 and self.heap[self.parent(idx)] < self.heap[idx]:
            self.heap[self.parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.parent(idx)]
            idx = self.parent(idx)

    def extract(self):
        if not self.heap: return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapify()
        return root

    def heapify(self,idx=0):
        lg = idx
        left = self.leftChild(idx)
        right = self.rightChild(idx)

        if left < len(self.heap) and self.heap[left] > self.heap[lg]:
            lg = left
        if right < len(self.heap) and self.heap[right] > self.heap[lg]:
            lg = right

        if lg != idx:
            self.heap[lg], self.heap[idx] = self.heap[idx], self.heap[lg]
            self.heapify(lg)

    def peek(self):
        return self.heap[0]

    def buildHeap(self, arr):
        self.heap = arr
        for i in range((len(arr)//2)-1,-1,-1):
            self.heapify(i)

    def size(self):
        return len(self.heap)

# find kth largest element in an array
class kthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.minHeap = MinHeap()
        for num in nums:
            self.add(num)

    def add(self, num):
        if self.minHeap.size() < self.k:
            self.minHeap.insert(num)
        elif num > self.minHeap.peek():
            self.minHeap.extract()
            self.minHeap.insert(num)
        return self.minHeap.peek()


# merge k sorted lists
def mergeKLists(lists):
    minHeap = []
    idx = [0 for _ in range(len(lists))]
    merged = []
    length = sum(len(lst) for lst in lists)
    for i in range(len(lists)):
        heapq.heappush(minHeap, (lists[i][idx[i]],i))
        idx[i] += 1
    while len(merged) < length:
        smallest,id = heapq.heappop(minHeap)
        merged.append(smallest)
        heapq.heappush(minHeap,(lists[id][idx[id]],id))
        idx[id] += 1
        if idx[id] >= len(lists[id]):
            continue
    return merged


    while minHeap.size() > 0:
        merged.append(minHeap.extract())
    return merged

# top k frequent elements
def topKFrequent(num,k):
    from collections import Counter
    count = Counter(num)
    minHeap = []
    for key in count:
        heapq.heappush(minHeap, (count[key], key))
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    res = []
    while len(minHeap) > 0:
        res.append(heapq.heappop(minHeap)[1])
    return res[::-1]


# find median from data stream
class MedianFinder:
    def __init__(self):
        self.maxHeap = MaxHeap()
        self.minHeap = MinHeap()

    def add(self, num):
        if self.maxHeap.size() == 0 or num <= self.maxHeap.peek():
            self.maxHeap.insert(num)
        else: self.minHeap.insert(num)

        if self.maxHeap.size() > self.minHeap.size() + 1:
            self.minHeap.insert(self.maxHeap.extract())
        elif self.minHeap.size() > self.maxHeap.size():
            self.maxHeap.insert(self.minHeap.extract())

    def findMed(self):
        if self.maxHeap.size() > self.minHeap.size():
            return self.maxHeap.peek()
        return (self.maxHeap.peek() + self.minHeap.peek()) / 2

# sliding window median
class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap = MaxHeap() # lower half
        self.minHeap = MinHeap() # upper half
        self.delayed = {}
        self.maxHeapSize = 0
        self.minHeapSize = 0

    def addNum(self, num):
        if self.maxHeap.size() == 0 or num <= self.maxHeap.peek():
            self.maxHeap.insert(num)
            self.maxHeapSize += 1
        else:
            self.minHeap.insert(num)
            self.minHeapSize += 1
        self.balanceHeaps()

    def removeNum(self, num):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if num <= self.maxHeap.peek():
            self.maxHeapSize -= 1
            if num == self.maxHeap.peek():
                self.prune(self.maxHeap)
        else:
            self.minHeapSize -= 1
            if num == self.minHeap.peek():
                self.prune(self.minHeap)
        self.balanceHeaps()

    def prune(self, heap):
        while heap.size() > 0 and heap.peek() in self.delayed:
            top = heap.peek()
            if top in self.delayed:
                if self.delayed[top] > 1:
                    self.delayed[top] -= 1
                else:
                    del self.delayed[top]
                heap.extract()
            else:
                break

    def balanceHeaps(self):
        if self.maxHeapSize > self.minHeapSize + 1:
            self.minHeap.insert(self.maxHeap.extract())
            self.maxHeapSize -= 1
            self.minHeapSize += 1
            self.prune(self.maxHeap)
        elif self.minHeapSize > self.maxHeapSize:
            self.maxHeap.insert(self.minHeap.extract())
            self.minHeapSize -= 1
            self.maxHeapSize += 1
            self.prune(self.minHeap)

    def findMedian(self):
        if self.maxHeapSize > self.minHeapSize:
            return float(self.maxHeap.peek())
        return (self.maxHeap.peek() + self.minHeap.peek()) / 2.0
# Smallest Range Covering Elements from K Lists
class SmallestRange:
    def smallestRange(self, nums):
        minHeap = []
        maxVal = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            maxVal = max(maxVal, nums[i][0])
        res = [float('-inf'), float('inf')]
        while len(minHeap) == len(nums):
            minVal, listId, eleId = heapq.heappop(minHeap)
            if maxVal - minVal < res[1] - res[0]:
                res = [minVal, maxVal]
            if eleId + 1 < len(nums[listId]):
                nextVal = nums[listId][eleId + 1]
                heapq.heappush(minHeap, (nextVal, listId, eleId + 1))
                maxVal = max(maxVal, nextVal)
        return res

# Dijkstra's algorithm
def dijkstra(graph, source):
    # graph: adjacency list {node: [(neighbor, weight), ...]}
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    min_heap = [(0, source)]  # (distance, node)

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        if current_dist > dist[u]:
            continue  # Skip outdated entry

        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(min_heap, (new_dist, v))

    return dist


# Huffman Encoding

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(freq_map):
    heap = [Node(freq, char) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heap[0]

    codes = {}
    def generate_codes(node, code=""):
        if node.char is not None:
            codes[node.char] = code
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root)
    return codes
