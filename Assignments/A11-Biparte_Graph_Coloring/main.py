class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [0]*(n+1)
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color
            
            colors[node] = color

            for nei in graph[node]:
                if not dfs(nei, -color):
                    return False
            
            return True
        
        for i in range(1, n+1):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
        
        return True
