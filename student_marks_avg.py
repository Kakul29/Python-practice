n = int(input())
marks = {}
for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        marks[name] = scores
query_name = input()
avg = sum(marks[query_name]) / len(marks[query_name])
print(f"{avg:.2f}")

        