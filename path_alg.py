# This algorithm takes a graph of nodes to values and maps those nodes with other nodes that
# have shared values, weighs the connection between them based on the number of 
# values they have in common, and also calculates the number of hops
# this algorithm is a hop and weight identifying algorithm
# Per completion of graph, values are called by paths[start][desired_node]
# a dictionary of { hops: total_path_weight } is the output


def weight(graph, n1, n2):
        weight = []
        for i in graph[n1]:
                for e in graph[n2]:
                        if i == e and i not in weight:
                                weight.append(i)
        return 1.0/float(len(weight))

def shortest_path_by_weight(graph, start, paths):
    open_list = []
    paths[start] = {}
    paths[start][start] = {0: 0}
    for i in graph[start]:
            for e in graph.keys():
                    if i in graph[e]:
                            if e not in open_list:
                                    open_list.append(e)
                                    paths[start][e] = { 1 : weight(graph, start, e) }
    while len(open_list) > 0:
            current = open_list[0]
            del open_list[0]
            for i in graph[current]:
                    for e in graph.keys():
                            if i in graph[e]:
                                    if e not in paths[start]:
                                            paths[start][e] = { int(str(paths[start][current].keys())[1]) + 1 : paths[start][current][int(str(paths[start][current].keys())[1])] + weight(graph, current, e) }
                                            open_list.append(e)
                                    elif e in paths[start]:
                                            if int(str(paths[start][e].keys())[1]) - int(str(paths[start][current].keys())[1]) == 1:
                                                    if paths[start][e][int(str(paths[start][e].keys())[1])] > paths[start][current][int(str(paths[start][current].keys())[1])] + weight(graph, current, e):
                                                            paths[start][e][int(str(paths[start][e].keys())[1])] = paths[start][current][int(str(paths[start][current].keys())[1])] + weight(graph, current, e)
    return "Your weighted graph has been created"
    
# the newest version of a short_path algorithm I wrote which gives the literal
# path as a graph as well as the weighted path
# the literal path is, of course, created from the weighted path
    
    def shortest_by_weight(graph, start):
    char_graph = {}
    weight_graph = {}
    char_graph[start] = {}
    weight_graph[start] = {}
    open_list = []
    for i in graph[start]:
        for e in graph.keys():
                if i in graph[e]:
                    if e not in open_list or weight_graph[start]:
                        open_list.append(e)
                        weight_graph[start][e] = weight(graph, start, e)
                        char_graph[start][e] = [start, e]
    while len(open_list) > 0:
        curr = open_list[0]
        del open_list[0]
        for i in graph[curr]:
            for e in graph.keys():
                if i in graph[e]:
                    if e not in weight_graph[start]:
                        weight_graph[start][e] = weight_graph[start][curr] + weight(graph,curr,e)
                        char_graph[start][e] = char_graph[start][curr] + [e]
                        open_list.append(e)
                    elif e in weight_graph[start] and weight_graph[start][e] > weight_graph[start][curr] + weight(graph,curr,e):
                        weight_graph[start][e] = weight_graph[start][curr] + weight(graph,curr,e)
                        char_graph[start][e] = char_graph[start][curr] + [e]
    return char_graph
    
