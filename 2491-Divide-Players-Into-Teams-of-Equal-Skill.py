class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        chemistry =0

        target_sum = skill[0]+skill[-1]

        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1]!=target_sum:
                return -1

            chemistry += skill[i]*skill[-i-1]
        return chemistry
        