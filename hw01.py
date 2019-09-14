for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i}*{j}={i*j:<2d}", end='  ')
    print()
    print("        "*i, end='')
