class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for num in arr:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        return len(set(dict.values())) == len(dict.values())
