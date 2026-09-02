# use walrus operator to assign and check a value in a single expression


if (n := len([1,23,4,5,6,7,8,9,10,11])) > 10:    
    print(f"List is too long ({n} elements, expected <= 10)")