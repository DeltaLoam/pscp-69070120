"""bunny"""

bunny_count = int(input())
SCORE = []

for _ in range(bunny_count):
    score = int(input())
    SCORE.append(score)

print(max(SCORE))
print(SCORE.count(max(SCORE)))
