with open("input_2.txt") as f:
    input_data = f.readlines()

import networkx

graph = networkx.Graph()

for connection in input_data:
    f, t = connection.strip().split("-")
    graph.add_edge(f, t)

out = 0
for clique in networkx.enumerate_all_cliques(graph):
    if len(clique) == 3 and any([x for x in clique if x.startswith("t")]):
        print(clique)
        out += 1
print(out)
