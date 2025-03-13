class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # Initialize the heap

        # Add the first k elements to the heap
        for i in range(k):
            heap.append(nums[i])

        # Convert the list into a min-heap
        heapq.heapify(heap)

        # Iterate through the remaining elements
        for i in range(k, len(nums)):
            if heap[0] < nums[i]:  # If the current element is larger than the smallest in the heap
                heapq.heappop(heap)  # Remove the smallest element
                heapq.heappush(heap, nums[i])  # Add the current element

        # The root of the heap is the kth largest element
        return heap[0]