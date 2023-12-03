# 1002. Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonChar = []
        countObj = {}

        for char in words[0]:
            countObj[char] = countObj.get(char, 0) + 1

        for word in words[1:]:
            currCount = {}

            for letter in word:
                currCount[letter] = currCount.get(letter, 0) + 1

            for letter in countObj.copy():
                if letter in currCount:
                    countObj[letter] = min(countObj[letter], currCount[letter])
                else:
                    countObj.pop(letter)

        for key, value in countObj.items():
            commonChar.extend([key] * value)

        return commonChar

//
