def eratosthenes(limit):
    # Create an array containing numbers from 1 to limit
    primes = []
    for i in range(2, limit):
        primes.append(i)

    # Loop through the numbers removing composites of the found primes
    for y in primes:
        for i in primes:
            if i % y == 0:
                if i != y:
                    primes.remove(i)

    print("Primes up to " + str(limit) + ":")
    print(str(primes))
    return primes