def pyramid(number):
    if type(number) not in [int]:
        print("It is impossible")

    if number <= 0:
        print("It is impossible")

    k = 1
    while True:
        total = k * (k + 1) * (2 * k + 1) // 6
        
        if total == number:
            return k
        elif total > number:
            return "It is impossible"
        k += 1