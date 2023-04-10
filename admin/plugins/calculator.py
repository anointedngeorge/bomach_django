

def function1(data=dict):
    total = 0
    for x in data.values():
        total =  total + int(x)
    return total