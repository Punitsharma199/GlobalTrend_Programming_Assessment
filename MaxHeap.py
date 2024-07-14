class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        if len(self.heap) == 0:
            raise IndexError("delete from empty heap")
        idx = self.heap.index(val)
        self._swap(idx, len(self.heap) - 1)
        self.heap.remove(val)
        self._heapify_down(idx)

    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("get_max from empty heap")
        return self.heap[0]

    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[parent] < self.heap[idx]:
            self._swap(parent, idx)
            self._heapify_up(parent)

    def _heapify_down(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self._swap(idx, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Example usage
heap = MaxHeap()
heap.insert(5)
heap.insert(12)
heap.insert(3)
print(heap.heap)  # Output: [12, 5, 3]
print(heap.get_max())  # Output: 12

heap.delete(5)
print(heap.heap)  # Output: [12, 3]
print(heap.get_max())  # Output: 12

