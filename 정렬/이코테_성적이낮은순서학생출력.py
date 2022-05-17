N = int(input())
STUDENT = []
for _ in range(N):
    name, score = map(str, input().split());
    STUDENT.append((name, int(score)))

STUDENT.sort(key=lambda a:a[1])

for s in STUDENT:
    print(s[0], end = " ")