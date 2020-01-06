def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def deal(lines):
    new_lines = []
    person = None
    for i in lines:
        if i == 'Allen':
            person = 'Allen'
            continue
        elif i == 'Tom':
            person = 'Tom'
            continue
        if person:
            new_lines.append(person + ': ' + i)
    return new_lines

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = deal(lines)
    write_file('output.txt', lines)

main()