# Problem: String Formatting
# Source: HackerRank

def print_formatted(number):
    width = len(format(number, 'b'))

    for i in range(1, number + 1):
        print(
            f"{i:>{width}} "
            f"{i:>{width}o} "
            f"{i:>{width}X} "
            f"{i:>{width}b}"
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
