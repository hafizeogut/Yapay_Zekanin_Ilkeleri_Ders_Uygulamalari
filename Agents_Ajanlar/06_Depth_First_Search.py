graph = {
    "A": {"B": 1, "C": 2},
    "B": {"A": 3, "C": 4},
    "C": {"A": 5, "B": 6}
}

def dfs(start,goal):
    visited=set()#boş küme oluituruluyor
    stack=[(start,[start])]
    print("stack",stack)
    while stack:
        node,path=stack.pop()
        
        print("Node: ",node)
        print("path: ",path)
        
        #Gçnderilen hedefe dğpğm eşitse:
        if node==goal:
            return path
        
        #düğüm zşyaret  edilmemişse
        if node not in visited:
            visited.add(node)
            
            for neigbor,cost in graph[node].items():
                #komşu,maliyet
                #items sozlukteki anahtar değer ikilisini bir liste olarak döndürür.
                print("komsu",neigbor)
                print("maliyet",cost)
                if neigbor not in visited:
                    stack.append((neigbor,path+[neigbor]))
    return None

start = "A"
goal = "C"
path = dfs(start, goal)
print(path)