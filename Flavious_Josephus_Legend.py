
testCases = int(input())

results = []

for i in range(testCases):
    n, k = input().split(' ')
    size = int(n)
    skip = int(k)

    sucideSquad = []
    for n in range(size):
        if n != skip-1:
            sucideSquad.append(1)
        else:
            sucideSquad.append(0)
    
    lastSuicide = skip
    k = 0
    suicides = 1
    while suicides < size - 1:
        for j in range(lastSuicide, size):

            if sucideSquad[j]:
                k += 1

            if k < skip:
                if j == size-1:
                    j = 0

            if k == skip:
                lastSuicide = j
                sucideSquad[j] = 0
                suicides += 1
