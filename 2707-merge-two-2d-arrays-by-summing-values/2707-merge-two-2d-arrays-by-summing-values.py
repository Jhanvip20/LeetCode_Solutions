class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = {}
        
        # Add values from the first array
        for id, value in nums1:
            if id in result:
                result[id] += value
            else:
                result[id] = value
        
        # Add values from the second array
        for id, value in nums2:
            if id in result:
                result[id] += value
            else:
                result[id] = value
        
        # Convert the dictionary to a list of lists and sort by id
        merged_result = [[id, value] for id, value in result.items()]
        merged_result.sort(key=lambda x: x[0])  # Sort by id
        
        return merged_result