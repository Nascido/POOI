
testCases = int(input())

results = []

for i in range(testCases):
    n, k = input().split(' ')
    size = int(n)
    skip = int(k)

    suicideSquad = []
    for n in range(size):
        if n != skip-1:
            suicideSquad.append(1)
        else:
            suicideSquad.append(0)
    
    start = skip
    k = 0
    suicides = 1
    
    while k < skip:
        for j in range(start, size):

            if suicideSquad[j]:
                k += 1

            if k < skip:
                if j == size-1:
                    start = 0

            if k == skip:
                start = j
                suicideSquad[j] = 0
                suicides += 1
                if suicides < size-1:
                    k = 0
                else:
                    break

    saved = suicideSquad.index(1) + 1
    results.append(saved)

i = 1
for saved in results:
    print(f"Case {i}: {saved}")
    i += 1
