test_dict = {
    "music": {"x": 5, "y": 6, "z": 3},
    "best": {"x": 8, "y": 3, "z": 5}
}

res = {}

for outer_key, inner_dict in test_dict.items():
    for key, val in inner_dict.items():
        if key not in res:
            res[key] = []
        res[key].append((outer_key, val))

print(res)
