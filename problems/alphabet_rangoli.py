# Problem: Alphabet Rangoli
# Source: HackerRank

def print_rangoli(size):
    width = 4 * size - 3

    # Top half
    for i in range(size-1, 0, -1):
        row = []

        for j in range(size-1, i-1, -1):
            row.append(chr(97 + j))

        for j in range(i+1, size):
            row.append(chr(97 + j))

        print('-'.join(row).center(width, '-'))

    # Middle row
    row = []

    for j in range(size-1, -1, -1):
        row.append(chr(97 + j))

    for j in range(1, size):
        row.append(chr(97 + j))

    print('-'.join(row).center(width, '-'))

    # Bottom half
    for i in range(1, size):
        row = []

        for j in range(size-1, i-1, -1):
            row.append(chr(97 + j))

        for j in range(i+1, size):
            row.append(chr(97 + j))

        print('-'.join(row).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
