class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():  
            return False

        vowels = set('aeiouAEIOU')
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

        has_vowel = any(char in vowels for char in word)
        has_consonant = any(char in consonants for char in word)

        if not has_vowel:
            return False

        if not has_consonant:
            return False

        return True
