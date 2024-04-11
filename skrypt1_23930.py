import numbers

def task1a(char): 
    if len(char) < 1:
        return False
    return char[0].isnumeric()
    

def task1b(char): # sprawdzi czy jest DOKLADNIE liczba, czyli "3" = False, 3 = True
    return isinstance(char, numbers.Number)

if __name__ == "__main__":
    inp = input("podaj znak: ")
    print( task1a(inp))
    print( task1b(inp))

