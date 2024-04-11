import random
import string

def task6():
    dictionary23930 = {}
    empty = ""
    for i in range(10, 21):
        dictionary23930[i] = empty.join(random.choices(string.ascii_lowercase,k=8))
        
    return dictionary23930

if __name__ == "__main__":
    print( task6())

