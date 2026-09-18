class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        mp = Counter(hand)

        while mp:

            curr = min(mp)

            for i in range(groupSize):

                if curr + i not in mp:
                    return False

                mp[curr + i] -= 1

                if mp[curr + i] == 0:
                    del mp[curr + i]

        return True
