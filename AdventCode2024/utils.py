def read_two_column_file(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(int(p[0]))
            y.append(int(p[1]))

    return x, y