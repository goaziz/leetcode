from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)

        for i, j in c.items():
            if i == 'R':
                if j != moves.count('L'):
                    return False
            elif i == 'L':
                if j != moves.count('R'):
                    return False
            elif i == 'U':
                if j != moves.count('D'):
                    return False
            elif i == 'D':
                if j != moves.count('U'):
                    return False

        return True

    def judgeCircle2(self, moves: str) -> bool:
        x, y = 0, 0

        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        return x == 0 and y == 0


obj = Solution()
moves = 'RLUD'
print(obj.judgeCircle2(moves))
