class Solution:
    def allPathsSourceTarget(self, graph):
        
        mem=[ [] for i in range(len(graph))]
        self.util(0,graph,mem)
        return mem[0]
    
    def util(self,node,graph,mem):

        if len(mem[node])>0:
            return mem[node]

        if(node == len(graph)-1):
            return [[len(graph)-1]]

        for i in range(len(graph[node])):

            temp=self.util(graph[node][i],graph,mem)


            for pth in temp:
                mem[node].append([node]+pth)

        return mem[node]