with open("input_2.txt") as f:
    input_data = f.readlines()

import networkx

graph = networkx.Graph()

for connection in input_data:
    f, t = connection.strip().split("-")
    graph.add_edge(f, t)

out = 0
print(gr := max(networkx.find_cliques(graph), key=len))
print(",".join(list(sorted(gr))))
print(out)
