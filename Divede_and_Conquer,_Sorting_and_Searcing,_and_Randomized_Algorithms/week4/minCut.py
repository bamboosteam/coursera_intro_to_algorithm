# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200.
# The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to.
# So for example, the 6th row looks like : "6	155	56	52	120	......".
# This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
#
# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.
# (HINT: Note that you'll have to figure out an implementation of edge contractions.  Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.  But you should also think about more efficient implementations.)
# (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)
# Write your numeric answer in the space provided.  So e.g., if your answer is 5, just type 5 in the space provided.
import random

def txt_to_array(path):
    test_file = open(path, "r")
    lines = test_file.read().splitlines()
    return lines

def read_graph(path):
    test_file = open(path, "r")
    lines = test_file.readlines()
    graph = []
    for i in range(len(lines)):
        tmp = lines[i].splitlines()
        index = tmp[0].split("\t")
        if index[-1] == '':
            index.pop()
        graph.append(index)
    return graph

graph = read_graph("kargerMinCut.txt")

def random_contraction(graph):
    n = len(graph)
    verticies_list = [graph[i][0] for i in range(n)]
    # base case: return the number of edges between the two verticies
    if n == 2:
        return len(graph[0] - 1)
    else:
        # radomly choose a remaining edge
        # edge is represented by node1 - node2
        node1 = random.choice(verticies_list)
        verticies = graph[verticies_list.index(node1)]
        node2 = random.choice(verticies[1:])
        # merge node1 and node2 into a single vertex
        # let node2 to be the vertex wchich will be merged.
        # add pair verticies of node2 to node1


        return node1, node2, verticies

print(random_contraction(graph))
