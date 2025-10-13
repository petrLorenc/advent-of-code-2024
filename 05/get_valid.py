with open("input.txt", "r") as f:
    input_data = f.read()
    rules, pages = input_data.split("\n\n")

rules_mapping = {}
counter = 0

for rule in rules.split("\n"):
    upper, lower = rule.split("|")
    rules_mapping.setdefault(upper, []).append(lower)

for page in pages.split("\n"):
    valid = True
    split_page = page.split(",")
    on_page: list = split_page.copy()
    for p in split_page:
        on_page.pop(0)
        should_be_lower = rules_mapping.get(p, [])
        for on_p in on_page:
            if on_p not in should_be_lower:
                valid = False
    if valid:
        counter += int(split_page[len(split_page) // 2])
print(rules_mapping)
print(counter)
