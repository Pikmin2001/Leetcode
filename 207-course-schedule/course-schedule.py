class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = set()
        CrsMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            CrsMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:      #loop found, false
                return False
            if CrsMap[crs] == []:    #no prereqs, we can take this one
                return True
            
                                    #continue if there is a prereq to explore
            visited.add(crs)
            for pre in CrsMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            CrsMap[crs] = []
            return True         #send back True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True