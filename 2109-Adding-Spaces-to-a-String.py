class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []                   
        it = 0                        

        for i, char in enumerate(s):
            if it < len(spaces) and i == spaces[it]: 
                result.append(' ')
                it += 1
            result.append(char)       

        return ''.join(result)        