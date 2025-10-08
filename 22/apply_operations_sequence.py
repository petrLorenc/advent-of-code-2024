from collections import defaultdict

with open("input.txt") as f:
    input_data = f.readlines()

input_data = list(map(str.strip, input_data))
input_data = list(map(int, input_data))

out = 0

sequences = []
sequences_diff = []

for number in input_data:
    print(number)
    sequence = [int(str(number)[-1])]
    for i in range(2000):
        number_64 = number * 64
        number_64_mix = number_64 ^ number
        number_64_mix = number_64_mix % 16777216

        number_32 = number_64_mix // 32
        number_32_mix = number_32 ^ number_64_mix
        number_32_mix = number_32_mix % 16777216

        number_2048 = number_32_mix * 2048
        number_2048_mix = number_2048 ^ number_32_mix
        number_2048_mix = number_2048_mix % 16777216

        number = number_2048_mix
        sequence.append(int(str(number)[-1]))
    sequences.append(sequence)
    sequence_diff = [y - x for x, y in zip(sequence, sequence[1:])]
    sequences_diff.append(sequence_diff)

# print(sequences[0])
# print(sequences[1])
# print(sequences[2])
# print(sequences[3])
# print(sequences_diff[0])
# print(sequences_diff[1])
# print(sequences_diff[2])
# print(sequences_diff[3])

sequences_diff_str = []
for s in sequences_diff:
    sequences_diff_str.append("".join(map(str, s)))

def get_return_for_sequence(seq, sequences, sequences_diff_str: list[str]):
    return_value = 0
    for idx, s in enumerate(sequences_diff_str):
        try:
            index = s.index(seq)
            index = len(s[:index].replace("-", ""))
            return_value += sequences[idx][index + len(seq.replace("-", ""))]
            # print(sequences[idx][index + len(seq.replace("-", ""))])
        except ValueError:
            continue
    return return_value


# max_return = 0
# for first in range(-9, 10):
#     for second in range(-9, 10):
#         for third in range(-9, 10):
#             for fourth in range(-9, 10):
#                 seq = f"{first}{second}{third}{fourth}"
#                 if max_return < (possible_new_max := get_return_for_sequence(seq, sequences, sequences_diff_str)):
#                     max_return = possible_new_max
#                     print(seq, max_return)

amounts = defaultdict(int)
for buyer_idx, change in enumerate(sequences_diff):
    keys = set()
    for i in range(len(change) - 3):
        key = tuple(change[i: i + 4])
        if key in keys:
            continue
        amounts[key] += sequences[buyer_idx][i + 4]
        keys.add(key)
max_return = max(amounts.values())
print(max_return)