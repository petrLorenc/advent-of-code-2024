with open("input_2.txt") as f:
    input_data = f.readlines()

memory = []
memory_size = 70 + 1
steps = 1024
for _ in range(memory_size):
    memory.append([0] * memory_size)


def print_memory(memory):
    for row in memory:
        print("".join([f"{str(x):^6}" for x in row]))


# print_memory(memory)

for byte in input_data[:steps]:
    x, y = byte.strip().split(",")
    memory[int(y)][int(x)] += 1

# print()
# print_memory(memory)

cost = [[0 for x in range(memory_size)] for y in range(memory_size)]
visited = [[0 for x in range(memory_size)] for y in range(memory_size)]


def get_cost(memory, cost, start, end):
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return cost[x][y]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < memory_size
                and 0 <= new_y < memory_size
                and memory[new_y][new_x] == 0
            ):
                if cost[new_y][new_x] > cost[y][x] + 1 or visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    cost[new_y][new_x] = cost[y][x] + 1
                    queue.append((new_x, new_y))
                    # print_memory(cost)
                    # print()


print(get_cost(memory, cost, (0, 0), (memory_size - 1, memory_size - 1)))
# print()
print_memory(cost)
#
# def get_path(start, end, cost):
#     start_x, start_y = start
#     end_x, end_y = end
#     path = [(start_x, start_y)]
#     while (start_x, start_y) != (end_x, end_y):
#         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             new_x, new_y = start_x + dx, start_y + dy
#             if 0 <= new_x < memory_size and 0 <= new_y < memory_size and cost[new_y][new_x] < cost[start_y][start_x]:
#                 path.append((new_x, new_y))
#                 start_x, start_y = new_x, new_y
#                 break
#     return path
#
# print(get_path((6, 6), (0, 0), cost))
