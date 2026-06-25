def mean(data):

    return sum(data) / len(data)


def variance(data):

    avg = mean(data)

    total = 0

    for num in data:
        total += (num - avg) ** 2

    return total / len(data)


def normalize(data):

    min_val = min(data)
    max_val = max(data)

    result = []

    for num in data:
        value = (num - min_val) / (max_val - min_val)
        result.append(value)

    return result