import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test != '\n':
        test = test.strip()
        numbers = test.split(',')
        x = int(numbers[0])
        n = int(numbers[1])
        multiplier = n

        while n < x:
            n += multiplier
            if n >= x:
                print n
