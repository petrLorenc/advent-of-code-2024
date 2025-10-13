import nltk

with open("input_2.txt") as f:
    input_data = f.readlines()

options = input_data[0]
designs = input_data[2:]

grammar_str = "A -> A B | B\nB -> "

for option in options.split(","):
    for ch in option.strip():
        grammar_str += f"'{ch}' "
    grammar_str += "| "

print(grammar_str[:-2])  # remove | at the end
grammar = nltk.CFG.fromstring(grammar_str[:-2])  # remove | at the end

designs = map(str.strip, designs)

#
# def try_pattern(design: str, option_mapping: dict):
#     if design == "":
#         return True
#     response = False
#     for pattern in option_mapping.get(design[0], []):
#         if design.startswith(pattern):
#             response = response or try_pattern(design[len(pattern):], option_mapping)
#         if response:
#             return response
#     return response


# print(sum([1 for design in designs if try_pattern(design, option_mapping)]))
cnt = 0
parser = nltk.ChartParser(grammar)

for design in designs:
    trees = list(parser.parse(design))
    if trees:
        cnt += 1
        print(trees[0])
print(cnt)
