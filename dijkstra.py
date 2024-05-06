def dijkstra(source,G):
    cost={}

    INFINITY=float('inf')
    cost[source]=0
    unvisited_list=list(G.keys())
    
    for vertex in G:
        if vertex!=source:
            cost[vertex]=INFINITY
            
    while unvisited_list:
        v=min(unvisited_list,key=lambda x:cost[x])
        
        unvisited_list.remove(v)
        
        for u in G[v]:
            cost_value=min(cost[u],cost[v]+G[v][u])
            cost[u]=cost_value

    return cost
    
def main():
    G={
        'A':{'B':4,'C':1},
        'B':{'A':4,'C':2,'D':5},
        'C':{'A':1,'B':2,'D':2,'E':1},
        'D':{'B':5,'C':2,'E':3},
        'E':{'C':1,'D':3}
    }
    
    source=input("Enter source vertex: ")
    
    ans=dijkstra(source,G)
    
    print(ans)
    
main()
