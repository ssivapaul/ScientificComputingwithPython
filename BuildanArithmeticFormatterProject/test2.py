def operation(op, y):
    
    result = op+y
    print(type(result))
    result = int(result)
    print(type(result))
    return result

print(operation('-', '5'))