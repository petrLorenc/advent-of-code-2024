import networkx as nx

G = nx.DiGraph()

with open("input_3.txt") as f:
    input_data = f.read()

board = [list(x.strip()) for x in input_data.strip().split("\n")]
x_len = len(board[0])
y_len = len(board)


def print_board(board):
    for row in board:
        print("".join([f"{str(x):^6}" for x in row]))


raw_graph = [[None for x in range(x_len)] for y in range(y_len)]
raw_graph_reverse = {}
idx = 0
idx_start = None
idx_ends = None

for y in range(y_len):
    for x in range(x_len):
        if 0 <= x < x_len and 0 <= y < y_len and board[y][x] != "#":
            if board[y][x] == "E":
                idx_ends = idx
                G.add_node(idx)
                left = idx
                right = left
                up = left
                down = left
                idx += 1
            else:
                G.add_node(idx)
                left = idx
                idx = idx + 1

                G.add_node(idx)
                up = idx
                idx = idx + 1

                G.add_node(idx)
                right = idx
                if board[y][x] == "S":
                    idx_start = idx
                idx = idx + 1

                G.add_node(idx)
                down = idx
                idx = idx + 1

                G.add_edge(left, up, weight=1000)
                G.add_edge(up, left, weight=1000)

                G.add_edge(up, right, weight=1000)
                G.add_edge(right, up, weight=1000)

                G.add_edge(right, down, weight=1000)
                G.add_edge(down, right, weight=1000)

                G.add_edge(down, left, weight=1000)
                G.add_edge(left, down, weight=1000)

            raw_graph[y][x] = {"l": left, "u": up, "r": right, "d": down}
            raw_graph_reverse[left] = (x, y)
            raw_graph_reverse[up] = (x, y)
            raw_graph_reverse[right] = (x, y)
            raw_graph_reverse[down] = (x, y)
            #
            # center_node = 7  # Or any other node to be in the center
            # edge_nodes = set(G) - {center_node}
            # # Ensures the nodes around the circle are evenly distributed
            # pos = nx.circular_layout(G.subgraph(edge_nodes))
            # pos[center_node] = np.array([0, 0])  # manually specify node position
            # nx.draw(G, pos, with_labels=True)
            # plt.savefig(f"filename_{random.random()}.png")
            # plt.show()

for y in range(y_len):
    for x in range(x_len):
        if 0 <= x + 1 < x_len and board[y][x] != "#" and board[y][x + 1] != "#":
            G.add_edge(raw_graph[y][x]["l"], raw_graph[y][x + 1]["l"], weight=1)
            G.add_edge(raw_graph[y][x + 1]["r"], raw_graph[y][x]["r"], weight=1)

        if 0 <= y + 1 < y_len and board[y][x] != "#" and board[y + 1][x] != "#":
            G.add_edge(raw_graph[y][x]["u"], raw_graph[y + 1][x]["u"], weight=1)
            G.add_edge(raw_graph[y + 1][x]["d"], raw_graph[y][x]["d"], weight=1)
        # center_node = 7  # Or any other node to be in the center
        # edge_nodes = set(G) - {center_node}
        # # Ensures the nodes around the circle are evenly distributed
        # pos = nx.circular_layout(G.subgraph(edge_nodes))
        # pos[center_node] = np.array([0, 0])  # manually specify node position
        # nx.draw(G, pos, with_labels=True)
        # plt.savefig(f"filename_{random.random()}.png")
        # plt.show()


# importing networkx


# Part 1
print(nx.shortest_path_length(G, idx_start, idx_ends, weight="weight"))

paths = list(nx.all_shortest_paths(G, idx_start, idx_ends, weight="weight"))


def map_path_to_map(raw_graph_reverse, path):
    # [10, 9, 7, 5, 0]
    return list(set([raw_graph_reverse[idx] for idx in path]))


points = []
for path in paths:
    x = map_path_to_map(raw_graph_reverse, path)
    points.extend(x)
print(list(set(points)))
print(len(list(set(points))))

for x in nx.all_shortest_paths(G, idx_start, idx_ends, weight="weight"):
    print(x)
# Part2
print(
    len(
        {
            path
            for path in nx.all_shortest_paths(G, idx_start, idx_ends, weight="weight")
        }
    )
)
