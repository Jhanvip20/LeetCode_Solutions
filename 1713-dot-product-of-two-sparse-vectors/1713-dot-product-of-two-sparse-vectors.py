class SparseVector:
	def __init__(self, nums: List[int]):
		self.seen = {}
		for i, n in enumerate(nums):
			if n != 0:
				self.seen[i] = n              

	# Return the dotProduct of two sparse vectors
	def dotProduct(self, vec: 'SparseVector') -> int:
		res = 0
		for j, n in vec.seen.items():
			if j in self.seen:
				res += n * self.seen[j]
		return res
		