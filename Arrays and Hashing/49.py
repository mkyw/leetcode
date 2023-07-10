'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]] '''

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        
#         s_chars = list()
#         t_chars = list()
#         for i in s:
#             s_chars.append(i)
#         for j in t:
#             t_chars.append(j)

#         for x in s:
#             if x in t_chars:
#                 s_chars.remove(x)
#                 t_chars.remove(x)
#             else:
#                 return False

#         if len(t_chars) == 0:
#             return True
#         else:
#             return False

#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         groups = list()

#         i = 0
#         while i < len(strs):
#             a = [strs[i]]
#             j = i+1
#             while j < len(strs):
#                 if i != j and self.isAnagram(strs[i], strs[j]):
#                     a.append(strs[j])
#                     strs.pop(j)
#                     j -= 1
#                 j += 1
#             i += 1
#             groups.append(a)

#         return groups

from collections import defaultdict

class Solution:
    def groupAnagrams(self, str):
        a = defaultdict(list)
        for i in str:
            x = ''.join(sorted(i))
            a[x].append(i)
        return list(a.values())
        


test = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(test.groupAnagrams(strs))
