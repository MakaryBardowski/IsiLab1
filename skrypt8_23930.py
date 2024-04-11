import random
import string

def task8():
    empty = ""
    randomString =  empty.join(random.choices(string.ascii_lowercase,k=100))
    uniqueChars = set(randomString)
    dict = {}
    for i in uniqueChars:
        dict[i] = randomString.count(i)
        
    return [list(i) for i in dict.items()]
if __name__ == "__main__":
    print( task8())

