# The file contains the edges of a directed graph.
# Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
# So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646
#
# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.
#
# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces).
# So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms.
# Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes).  (Note also that your answer should not have any spaces in it.)
#
# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully.
# The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
import copy as cp

def read_graph(path):
    test_file = open(path, "r")
    lines = test_file.readlines()
    graph = []
    for i in range(len(lines)):
        tmp = lines[i].splitlines()
        index = tmp[0].split(" ")
        if index[-1] == '':
            index.pop()
        graph.append(index)
    return graph

def get_keys_from_value(dict, value):
	return [k for k, v in dict.items() if v == value]

graph = read_graph("test1.txt")
verticies_list = [graph[i][0] for i in range(len(graph))]
n = max(verticies_list)
explored_list = {}
for i in range(1, int(n)+1):
	explored_list[str(i)] = 0

# for i in reversed(range(1, 11)):
# 	print(i)

def DFS_Loop(graph):
	# initialization
	verticies_list = [graph[i][0] for i in range(len(graph))]
	n = max(verticies_list)
	t = 0  # for finishing times in first pass
	s = "" # for leader in second pass
	explored_list, finishing_times, local_explored = {}, {}, {}
	for i in range(1, int(n)+1):
		explored_list[str(i)], finishing_times[str(i)], local_explored[str(i)] = 0, 0, 0

	# start searching
	for i in reversed(range(1, int(n) + 1)):
		if explored_list[str(i)] == 0:
			s = str(i)
			finishing_node = ""
			while finishing_node != s:
				finishing_node = DFS(graph, s, explored_list)
				t += 1
				finishing_times[finishing_node] = t
				local_explored[finishing_node] = 1
				# by using copy module, we can avoid from using same objects with different name.
				explored_list = cp.copy(local_explored)

	return finishing_times



def DFS(graph, node, explored_list):
	verticies_list = [graph[i][0] for i in range(len(graph))]
	# mark node as explored
	explored_list[node] = 1
	# if all nodes are explored, search is done. well done.
	if 0 not in explored_list.values():
		return node
	# if not, we need to seach deep into the graph.
	# create index list for node
	index_list = [n for n, v in enumerate(verticies_list) if v == node]
	# extract candidates graph which contains the outgoing arcs from node
	candidates = [graph[i] for i in index_list]
	# search deeper...
	for i in candidates:
		if explored_list[i[1]] == 0:
			return DFS(graph, i[1], explored_list)
	return node

print(DFS_Loop(graph))

# explored_list["4"] = 1
# explored_list["1"] = 1
# explored_list["7"] = 1
# explored_list["6"] = 1
# explored_list["3"] = 1
# print(DFS(graph, "9", explored_list))

def count_SCCs(graph):
	length_graph = len(graph)
	n = graph[-1][0]
	# make graph_rev
	graph_rev = []
	for i in graph:
		graph_rev.append([i[1], i[0]])

	# run DFS_Loop on graph_rev to obtain finishing times.
	finishing_times = DFS_Loop(graph_rev)

	# run DFS_Loop on graph in terms of finishing times

	return graph_rev
