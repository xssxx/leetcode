# 2023.12.23

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))

        for c in path:
            if c == 'N':
                y += 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            elif c == 'S':
                y -= 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False