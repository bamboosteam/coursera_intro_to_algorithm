########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
# num_nodes = 875715
num_nodes = 13

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("test2.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

########################################################
# Implementing DFS with stack data structure.

def dfs(graph, start):
	visited[start] = True
	stack = [start]
	while stack:
		v = stack.pop()
		for i in graph[v]:
			if visited[i] == False:
				print(i)
				visited[i] = True
				stack.append(i)
	return stack, visited	

print(dfs(gr, 1))
