class Solution:
    def dfs(self, m, r, c, visited, total_to_visit, rows, cols):
        if not (0 <= r < rows and 0 <= c < cols): return
        if m[r][c] == 2:
            if len(visited) == total_to_visit + 1:
                self.paths += 1
            return
        elif m[r][c] == -1:
            return
        elif (r, c) in visited:
            return
        visited.add((r, c))
        self.dfs(m, r + 1, c, visited, total_to_visit, rows, cols)
        self.dfs(m, r - 1, c, visited, total_to_visit, rows, cols)
        self.dfs(m, r, c + 1, visited, total_to_visit, rows, cols)
        self.dfs(m, r, c - 1, visited, total_to_visit, rows, cols)
        visited.discard((r, c))

    def uniquePathsIII(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total_to_visit = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    total_to_visit += 1
                if grid[row][col] == 1:
                    x, y = row, col
        self.paths = 0
        self.dfs(grid, x, y, set(), total_to_visit, rows, cols)
        return self.paths