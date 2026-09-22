class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        counter = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for j in t:
            if j in counter:
                counter[j] += 1
            else:
                counter[j] = 1

        if count == counter:
            return True
        else:
            return False