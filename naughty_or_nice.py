def naughty_or_nice_list(*args, **kwargs):
    santas_dict = {"Nice": [], "Naughty": [], "Not found": []}

    first_list = args[0]
    santas_list = []
    for num, name in first_list:
        santas_list.append(num)
        santas_list.append(name)

    for el in args[1:]:
        number, command = el.split("-")
        number = int(number)
        counter = santas_list.count(number)
        if counter == 1:
            idx = santas_list.index(number)
            santas_dict[command].append(santas_list[idx + 1])
            del santas_list[idx:idx + 2]

    for key in kwargs:
        if key in santas_list:
            counter = santas_list.count(key)
            if counter == 1:
                kid_name = key
                behaviour = kwargs[key]
                santas_dict[behaviour].append(kid_name)
                idx = santas_list.index(kid_name)
                del santas_list[idx - 1:idx + 1]

    for el in santas_list[1::2]:
        santas_dict["Not found"].append(el)

    res = [f"{key}: {', '.join(value)}" for key, value in santas_dict.items() if len(value) > 0]
    return '\n'.join(res)