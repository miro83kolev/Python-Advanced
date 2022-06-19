def naughty_or_nice_list(kids,*args, **kwargs):
    nice_kids = []
    naughty_kids = []

    for command in args:
        num, status = command.split('-')
        num = int(num)
        name = None

        is_unique = False
        for kid_number, kid_name in kwargs:
            if num == kid_number and is_unique:
                is_unique = False
                break
            if num == kid_number:
                name = kid_name
                is_unique = True
        if is_unique:
            kids.remove(num, name)

            if status == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)
    return nice_kids, naughty_kids

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


