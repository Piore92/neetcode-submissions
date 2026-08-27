import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_amounts_dict = defaultdict(int)

        for num in nums:
            number_amounts_dict[num]+=1

        return heapq.nlargest(k, number_amounts_dict, key=number_amounts_dict.get)


