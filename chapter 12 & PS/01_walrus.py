# use walrus operator to assign and check a value in a single expression


if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"The length of the list is {n} elements, expected <= 3")