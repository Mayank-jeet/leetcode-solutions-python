#  *
#  * LeetCode: 207 - Course Schedule
#  * Link: https://leetcode.com/course-schedule/
#  * Difficulty: Medium
#  * Time: O(V+E) where V is number of vertices and E is number of edges
#  * Space: O(V)
#  *
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for _ in range(numCourses)]
        n=len(prerequisites)
        for i in range(n):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        inqueue=[0]*numCourses
        for i in range(numCourses):
            for j in range(len(adj[i])):
                inqueue[adj[i][j]]+=1
        q=deque()
        for i in range(numCourses):
            if inqueue[i]==0:
                q.append(i)
        topo=[]
        while(len(q)!=0):
            node=q[0]
            topo.append(node)
            q.popleft()
            for i in range(len(adj[node])):
                inqueue[adj[node][i]]-=1
                if inqueue[adj[node][i]]==0:
                    q.append(adj[node][i]) 
        return len(topo)==numCourses  