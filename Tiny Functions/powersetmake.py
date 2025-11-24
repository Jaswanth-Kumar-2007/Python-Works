def generate_sets(lst):
    result = [[]]

    for num in lst:
        new_sets = []
        for s in result:
            new_sets.append(s + [num])
        result.extend(new_sets)
        print(result)

generate_sets([1, 2, 3])
