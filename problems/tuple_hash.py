# Problem: Tuple Hash
# Source: HackerRank
# Note: hash() output may vary across Python versions. If you are doing it on hackerrank, switch to Python 2 and it will work

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
