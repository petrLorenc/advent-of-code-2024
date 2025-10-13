with open("input.txt", "r") as f:
    input_data = f.read()
    rules, pages = input_data.split("\n\n")

rules_mapping = {}
counter = 0
fixed = []

for rule in rules.split("\n"):
    upper, lower = rule.split("|")
    rules_mapping.setdefault(upper, []).append(lower)

for page in pages.split("\n"):
    valid = True
    split_page = page.split(",")
    fixed_page: list = page.split(",")
    for _ in range(10):  # artificially chosen
        for p in split_page:
            should_be_lower = rules_mapping.get(p, [])
            for rule in should_be_lower:
                if rule in fixed_page and fixed_page.index(rule) < fixed_page.index(p):
                    first = fixed_page.index(rule)
                    second = fixed_page.index(p)
                    fixed_page[first], fixed_page[second] = (
                        fixed_page[second],
                        fixed_page[first],
                    )
                    valid = False

    if not valid:
        fixed.append(fixed_page)


for pages in fixed:
    counter += int(pages[len(pages) // 2])

print(fixed)
print(rules_mapping)
print(counter)
