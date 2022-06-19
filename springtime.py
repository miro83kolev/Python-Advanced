def start_spring(**kwargs):
    result = ''
    my_dict = {}
    for key, value in kwargs.items():
        if not value in my_dict:
            my_dict[value] = []
        my_dict[value].append(key)

    sorted_dict = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_dict:
        type = tuple_[0]
        flower = tuple_[1]
        sorted_flowers = sorted(flower)
        result += f"{type}:\n"
        for flower in sorted_flowers:
            result += f"-{flower}\n"
    return result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

