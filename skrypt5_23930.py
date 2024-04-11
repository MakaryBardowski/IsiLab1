import math

def task5a(): 
    return [math.sqrt(i) for i in range(1, 257) if i % 2 == 0]

def task5b():
    roots = []
    for i in range(1, 257):
        if i % 2 == 0:
            roots.append(math.sqrt(i))
    return roots

if __name__ == "__main__":
    print( task5a())
    print( task5b())

