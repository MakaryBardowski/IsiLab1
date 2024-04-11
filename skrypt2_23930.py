import skrypt1_23930 as task1

def task2(string): # wywolujemy metode spradzajaca czy znak jest liczba dla kazdego znaku z task1
    return all(task1.task1a(char) for char in string)

if __name__ == "__main__":
    inp = input("podaj string: ")
    print( task2(inp))


