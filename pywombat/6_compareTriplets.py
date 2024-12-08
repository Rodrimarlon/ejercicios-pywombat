ana = [17, 28, 30]
bob = [99, 16, 8]


def compareTripletes(ana, bob):
    count_ana = 0
    count_bob = 0
    for a, b in zip(ana, bob):
        if a > b: 
            count_ana += 1
        elif a < b:
            count_bob += 1
        elif a == b:
            continue

    print(count_ana, count_bob)

compareTripletes(ana, bob)