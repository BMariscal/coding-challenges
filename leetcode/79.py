class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0

        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.bfs(x, y, idx, word, board):
                    return True
        return False

    def bfs(self, x, y, idx, word, board):
        char = board[x][y]
        if char != word[idx]:
            return False
        elif idx == len(word) - 1:
            return True

        board[x][y] = "*"

        if x > 0 and self.bfs(x - 1, y, idx + 1, word, board):
            return True
        if y > 0 and self.bfs(x, y - 1, idx + 1, word, board):
            return True

        if y < len(board[0]) - 1 and self.bfs(x, y + 1, idx + 1, word, board):
            return True

        if x < len(board) - 1 and self.bfs(x + 1, y, idx + 1, word, board):
            return True

        board[x][y] = word[idx]

        return False
