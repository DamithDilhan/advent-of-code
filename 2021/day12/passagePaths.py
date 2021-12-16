from collections import defaultdict, Counter
from copy import copy


class Graph():
    def __init__(self):
        self.V = 0
        self.graph = defaultdict(list)
        self.paths = 0
        self.path_list = []
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_paths(self):
        for key in self.graph:
            print(key,"-->")
            for node in self.graph[key]:
                print("\t",node)
    def __hash__(self,u):
        return self.graph[u]

    def printAllPathsUtil(self, u, d, visited,path):
        visited[u] = True
        path.append(u)
        if u==d:
            print(path)
            self.paths += 1
        
        for i in self.graph[u]:
            if i.isupper() or visited[i] == False:
                self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False

    def findRepeatables(self,content):
        temp = Counter([k for k in content if k.islower()])
        for i in temp.most_common():
            if i[0].islower() and i[1]==2:
                return True

        return False


    def printAllPathsUtil2(self,u, d, visited,path):

        visited[u] +=1
        path.append(u)
        if u==d:
            #print(path)
            self.paths += 1
        
        for i in self.graph[u]:
            if i.isupper() :
                self.printAllPathsUtil2(i, d, visited, path)

            elif i.lower() and self.findRepeatables(path) and visited[i] == 0 :
                self.printAllPathsUtil2(i, d,copy(visited), path)
            elif i.islower() and not self.findRepeatables(path):
                self.printAllPathsUtil2(i, d,copy(visited), path)
            
            

        path.pop()
        visited[u] = 0

    def printAllPaths(self,s,d):

        visited = { k:False for k in self.graph.keys()}
        path = []
        
        self.printAllPathsUtil(s,d,visited,path)
    
    def printAllPaths2(self,s,d):

        visited = { k:0 for k in self.graph.keys()}
        path = []
        
        self.printAllPathsUtil2(s,d,visited,path)






def find_route(u,i,v,graph,visited):
    
    if i.islower() and i in visited:
        return False
            



def find_start(content):
    start_points = []
    end_points = []
    paths = defaultdict(list)

    for row in content:
        if "start" in row:
            row.remove("start")
            start_points.append(row.pop())
        elif "end" in row:
            row.remove("end")
            end_points.append(row.pop())
        else:
            paths[row[0]].append(row[1])
            paths[row[1]].append(row[0])

    return start_points,end_points,paths


with open("input.txt", "r") as fp:
    content = list(map(lambda x: x.split("-") ,fp.read().splitlines()))


start_points, end_points, paths=find_start(content)

graph = Graph()
graph.graph = paths

for i in start_points:
    for e in end_points:
        graph.printAllPaths2(i,e)

print(graph.paths)
#130493





