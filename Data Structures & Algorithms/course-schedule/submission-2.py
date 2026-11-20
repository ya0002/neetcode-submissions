class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        if not prerequisites and numCourses:
            return True

        adj = defaultdict(set)

        for cr, pre in prerequisites:
            adj[cr].add(pre)

            # check if pre is a prequisite of cr==INMPOSSIBLE; detect non chained cycles
            if cr in adj[pre]:
                return False

        visited = set()

        def dfs(k):

            ## detect cycles
            if k in visited:
                return False

            visited.add(k)

            pres = adj[k].copy()
            for pre in pres:
                if dfs(pre):
                    adj[k].remove(pre)
                    visited.remove(pre)
                else:
                    return False
            
            ## a course can be done if all of its pres can be done==empty pre list
            if not adj[k]:
                return True

            return False

        for crs in adj.keys():
            if not dfs(crs):
                return False
            visited = set()

        return True
