class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_dict = defaultdict(list)

        for word in strs:

            key = "".join(sorted(word))

            anagrams_dict[key].append(word)

        return list(anagrams_dict.values())