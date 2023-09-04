
answers = []

while True:
    try:
        a, b = (input()).split(" ")
        abin = []
        bbin = []
        addbin = []

        a = int(a)
        b = int(b)
        while a != 0:
            abin.append(a%2)
            a = a//2
        
        while b != 0:
            bbin.append(b%2)
            b = b//2

        if len(abin) >= len(bbin):
            for i in range(len(bbin),len(abin)):
                bbin.append(0)
        else:
            for i in range(len(abin), len(bbin)):
                abin.append(0)

        abin.reverse()
        bbin.reverse()

        for i in range(len(abin)):
            if abin[i] == 1:
                if bbin[i] == 1:
                    addbin.append(0)
                else:
                    addbin.append(1)
            
            else:
                if bbin[i] == 1:
                    addbin.append(1)
                else:
                    addbin.append(0)
                
        add = 0
        addbin.reverse()

        for i in range(len(addbin)):
            add += addbin[i]*2**i

        answers.append(add)

    except EOFError:
        for add in answers:
            print(add)
        break
