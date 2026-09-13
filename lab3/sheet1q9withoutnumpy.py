marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
temperature = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]


def statistics(data):

    # Mean
    mean = sum(data) / len(data)

    # Median
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    # Standard deviation
    total = 0
    for x in data:
        total = total + (x - mean) ** 2

    variance = total / len(data)
    standard_deviation = variance ** 0.5

    # Minimum and maximum
    minimum = min(data)
    maximum = max(data)

    print("Mean =", mean)
    print("Median =", median)
    print("Standard Deviation =", standard_deviation)
    print("Minimum =", minimum)
    print("Maximum =", maximum)


print("MARKS")
statistics(marks)

print("\nTEMPERATURE")
statistics(temperature)