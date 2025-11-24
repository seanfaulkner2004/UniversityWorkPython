def print_numbered_lines(filename):
    """kgtvjhgtfvcjhgtc"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    lines = contents.splitlines()
    for line in lines:
        if 'crivens' in line:
            print(line)

print_numbered_lines('marks1.txt')