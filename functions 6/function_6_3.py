def simple_map(transformation, values):
    result = []
    for value in values:
        result.append(transformation(value))
    return result