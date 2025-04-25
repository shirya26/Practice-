def apply_function(data, func):
    return [func(item) for item in data]

def square(x):
    return x * x

result = apply_function([1, 2, 3], square)
print(result)  # Output: [1, 4, 9]
